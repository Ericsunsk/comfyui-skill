> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get asset metadata from remote URL

> Retrieves metadata for an asset from a remote download URL without downloading the entire file.
Supports various sources including CivitAI and other model repositories.
Uses HEAD requests or API calls to fetch metadata efficiently.
This endpoint is for previewing metadata before downloading, not for getting metadata of existing assets.




## OpenAPI

````yaml openapi-cloud.yaml get /api/assets/remote-metadata
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
  /api/assets/remote-metadata:
    get:
      tags:
        - asset
      summary: Get asset metadata from remote URL
      description: >
        Retrieves metadata for an asset from a remote download URL without
        downloading the entire file.

        Supports various sources including CivitAI and other model repositories.

        Uses HEAD requests or API calls to fetch metadata efficiently.

        This endpoint is for previewing metadata before downloading, not for
        getting metadata of existing assets.
      operationId: getRemoteAssetMetadata
      parameters:
        - name: url
          in: query
          required: true
          description: Download URL to retrieve metadata from
          schema:
            type: string
            format: uri
            example: https://civitai.com/api/download/models/123456
      responses:
        '200':
          description: Metadata retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetMetadataResponse'
        '400':
          description: Invalid URL or missing required parameter
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
          description: Failed to retrieve metadata from source
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
    AssetMetadataResponse:
      type: object
      required:
        - content_length
      properties:
        content_length:
          type: integer
          format: int64
          description: Size of the asset in bytes (-1 if unknown)
          example: 4294967296
        content_type:
          type: string
          description: MIME type of the asset
          example: application/octet-stream
        filename:
          type: string
          description: Suggested filename for the asset from source
          example: realistic-vision-v5.safetensors
        name:
          type: string
          description: Display name or title for the asset from source
          example: Realistic Vision v5.0
        tags:
          type: array
          items:
            type: string
          description: Tags for categorization from source
          example:
            - models
            - checkpoint
        preview_image:
          type: string
          description: Preview image as base64-encoded data URL
          example: data:image/jpeg;base64,/9j/4AAQSkZJRg...
        validation:
          $ref: '#/components/schemas/ValidationResult'
          description: Validation results for the file
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
    ValidationResult:
      type: object
      required:
        - is_valid
      properties:
        is_valid:
          type: boolean
          description: Overall validation status (true if all checks passed)
          example: true
        errors:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
          description: Blocking validation errors that prevent download
        warnings:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
          description: Non-blocking validation warnings (informational only)
    ValidationError:
      type: object
      required:
        - code
        - message
        - field
      properties:
        code:
          type: string
          description: Machine-readable error code
          example: FORMAT_NOT_ALLOWED
        message:
          type: string
          description: Human-readable error message
          example: >-
            File format "PickleTensor" is not allowed. Allowed formats:
            [SafeTensor]
        field:
          type: string
          description: Field that failed validation
          example: format
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