> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Initiate background download for large files

> Initiates a background download job for large files from Huggingface or Civitai.

If the file already exists in storage, the asset record is created immediately and returned (200 OK).
If the file doesn't exist, a background task is created and the task ID is returned (202 Accepted).
The frontend can track progress using GET /api/tasks/{task_id}.




## OpenAPI

````yaml openapi-cloud.yaml post /api/assets/download
openapi: 3.0.3
info:
  title: Comfy Cloud API
  description: >
    <Warning>

    **Experimental API:** This API is experimental and subject to change. 

    Endpoints, request/response formats, and behavior may be modified without
    notice.

    </Warning>


    API for Comfy Cloud - Run ComfyUI workflows on cloud infrastructure.


    This API allows you to interact with Comfy Cloud programmatically,
    including:

    - Submitting and managing workflows

    - Uploading and downloading files

    - Monitoring job status and progress


    ## Cloud vs OSS ComfyUI Compatibility


    Comfy Cloud implements the same API interfaces as OSS ComfyUI for maximum
    compatibility,

    but some fields are accepted for compatibility while being handled
    differently or ignored:


    | Field | Endpoints | Cloud Behavior |

    |-------|-----------|----------------|

    | `subfolder` | `/api/view`, `/api/upload/*` | **Ignored** - Cloud uses
    content-addressed storage (hash-based). Returned in responses for
    client-side organization. |

    | `type` (input/output/temp) | `/api/view`, `/api/upload/*` | Partially used
    - All files stored with tag-based organization rather than directory
    structure. |

    | `overwrite` | `/api/upload/*` | **Ignored** - Content-addressed storage
    means identical content always has the same hash. |

    | `number`, `front` | `/api/prompt` | **Ignored** - Cloud uses its own fair
    queue scheduling per user. |

    | `split`, `full_info` | `/api/userdata` | **Ignored** - Cloud always
    returns full file metadata. |


    These fields are retained in the API schema for drop-in compatibility with
    existing ComfyUI clients and workflows.
  version: 1.0.0
  license:
    name: GNU General Public License v3.0
    url: https://github.com/comfyanonymous/ComfyUI/blob/master/LICENSE
servers:
  - url: https://cloud.comfy.org
    description: Comfy Cloud API
security:
  - ApiKeyAuth: []
tags:
  - name: workflow
    description: |
      Submit workflows for execution and manage the execution queue.
      This is the primary way to run ComfyUI workflows on the cloud.
  - name: job
    description: |
      Monitor job status, view execution history, and manage running jobs.
      Jobs are created when you submit a workflow via POST /api/prompt.
  - name: asset
    description: |
      Upload, download, and manage persistent assets (images, models, outputs).
      Assets provide durable storage with tagging and metadata support.
  - name: file
    description: |
      Legacy file upload and download endpoints compatible with local ComfyUI.
      For new integrations, consider using the Assets API instead.
  - name: model
    description: |
      Browse available AI models. Models are pre-loaded on cloud infrastructure.
  - name: node
    description: |
      Get information about available ComfyUI nodes and their inputs/outputs.
      Useful for building dynamic workflow interfaces.
  - name: user
    description: |
      User account information and personal data storage.
  - name: system
    description: |
      Server status, health checks, and system information.
paths:
  /api/assets/download:
    post:
      tags:
        - asset
      summary: Initiate background download for large files
      description: >
        Initiates a background download job for large files from Huggingface or
        Civitai.


        If the file already exists in storage, the asset record is created
        immediately and returned (200 OK).

        If the file doesn't exist, a background task is created and the task ID
        is returned (202 Accepted).

        The frontend can track progress using GET /api/tasks/{task_id}.
      operationId: createAssetDownload
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - source_url
              properties:
                source_url:
                  type: string
                  format: uri
                  description: >-
                    URL of the file to download (must be from huggingface.co or
                    civitai.com)
                  example: >-
                    https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors
                tags:
                  type: array
                  items:
                    type: string
                  description: Optional tags for the asset (e.g., ["model", "checkpoint"])
                user_metadata:
                  type: object
                  additionalProperties: true
                  description: Optional user-defined metadata to attach to the asset
                preview_id:
                  type: string
                  format: uuid
                  description: >-
                    Optional preview asset ID to associate with the downloaded
                    asset
                  example: 550e8400-e29b-41d4-a716-446655440000
      responses:
        '200':
          description: File already exists in storage - asset created/returned immediately
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetCreated'
        '202':
          description: Accepted - Download task created and processing in background
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetDownloadResponse'
        '400':
          description: Invalid URL or unsupported source
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '422':
          description: Validation errors
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    AssetCreated:
      allOf:
        - $ref: '#/components/schemas/Asset'
        - type: object
          required:
            - created_new
          properties:
            created_new:
              type: boolean
              description: >-
                Whether this was a new asset creation (true) or returned
                existing (false)
    AssetDownloadResponse:
      type: object
      required:
        - task_id
        - status
      properties:
        task_id:
          type: string
          format: uuid
          description: Task ID for tracking download progress via GET /api/tasks/{task_id}
        status:
          type: string
          enum:
            - created
            - running
            - completed
            - failed
          description: Current task status
        message:
          type: string
          description: Human-readable message
          example: Download task created. Use task_id to track progress.
    ErrorResponse:
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: string
        message:
          type: string
    Asset:
      type: object
      required:
        - id
        - name
        - size
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the asset
        name:
          type: string
          description: Name of the asset file
        asset_hash:
          type: string
          description: Blake3 hash of the asset content
          pattern: ^blake3:[a-f0-9]{64}$
        size:
          type: integer
          format: int64
          description: Size of the asset in bytes
        mime_type:
          type: string
          description: MIME type of the asset
        tags:
          type: array
          items:
            type: string
          description: Tags associated with the asset
        user_metadata:
          type: object
          description: Custom user metadata for the asset
          additionalProperties: true
        preview_url:
          type: string
          format: uri
          description: URL for asset preview/thumbnail
        preview_id:
          type: string
          format: uuid
          description: ID of the preview asset if available
          nullable: true
        prompt_id:
          type: string
          format: uuid
          description: ID of the job/prompt that created this asset, if available
          nullable: true
        created_at:
          type: string
          format: date-time
          description: Timestamp when the asset was created
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the asset was last updated
        last_access_time:
          type: string
          format: date-time
          description: Timestamp when the asset was last accessed
        is_immutable:
          type: boolean
          description: Whether this asset is immutable (cannot be modified or deleted)
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: >
        API key authentication. Generate an API key from your account settings

        at https://platform.comfy.org/profile/api-keys. Pass the key in the
        X-API-Key header.

````