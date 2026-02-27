> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# View a file

> Retrieve and view a file from the ComfyUI file system.
This endpoint is typically used to view generated images or other output files.




## OpenAPI

````yaml openapi-cloud.yaml get /api/view
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
  /api/view:
    get:
      tags:
        - file
      summary: View a file
      description: >
        Retrieve and view a file from the ComfyUI file system.

        This endpoint is typically used to view generated images or other output
        files.
      operationId: viewFile
      parameters:
        - name: filename
          in: query
          required: true
          description: Name of the file to view
          schema:
            type: string
            example: ComfyUI_00004_.png
        - name: subfolder
          in: query
          required: false
          description: >
            Subfolder path where the file is located.

            **Note:** Accepted for ComfyUI API compatibility but **ignored** in
            cloud.

            Cloud uses content-addressed storage where assets are stored by hash
            only.

            The subfolder is client-side UI metadata and not used for storage
            lookup.
          schema:
            type: string
            example: tests/foo/bar
        - name: type
          in: query
          required: false
          description: >
            Type of file (e.g., output, input, temp).

            **Note:** In cloud, both `output` and `temp` files are stored in the
            same bucket.

            The type parameter is used for compatibility but storage location is
            determined by hash.
          schema:
            type: string
            example: output
        - name: fullpath
          in: query
          required: false
          description: Full path to the file (used for temp files)
          schema:
            type: string
        - name: format
          in: query
          required: false
          description: Format of the file
          schema:
            type: string
        - name: frame_rate
          in: query
          required: false
          description: Frame rate for video files
          schema:
            type: integer
        - name: workflow
          in: query
          required: false
          description: Workflow identifier
          schema:
            type: string
        - name: timestamp
          in: query
          required: false
          description: Timestamp parameter
          schema:
            type: integer
            example: '1234567890'
        - name: channel
          in: query
          required: false
          description: |
            Image channel to extract from PNG images.
            - 'rgb': Return only RGB channels (alpha set to fully opaque)
            - 'a' or 'alpha': Return alpha channel as grayscale image
            - If not specified, return original image unchanged via redirect
          schema:
            type: string
            example: rgb
      responses:
        '200':
          description: >-
            Success - File content returned (used when channel parameter is
            present)
          content:
            image/png:
              schema:
                type: string
                format: binary
                description: Processed PNG image with extracted channel
        '302':
          description: Redirect to GCS signed URL
          headers:
            Location:
              description: Signed URL to access the file in GCS
              schema:
                type: string
        '400':
          description: Invalid request parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: File not found or unauthorized
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