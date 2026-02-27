> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload or update a user data file

> Upload a file to a user's data directory. Optional query parameters allow
control over overwrite behavior and response detail.




## OpenAPI

````yaml openapi-cloud.yaml post /api/userdata/{file}
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
  /api/userdata/{file}:
    post:
      tags:
        - user
      summary: Upload or update a user data file
      description: >
        Upload a file to a user's data directory. Optional query parameters
        allow

        control over overwrite behavior and response detail.
      operationId: postUserdataFile
      parameters:
        - name: file
          in: path
          required: true
          description: The target file path (URL encoded if necessary).
          schema:
            type: string
        - name: overwrite
          in: query
          required: false
          description: If "false", prevents overwriting existing files. Defaults to "true".
          schema:
            type: string
            enum:
              - 'true'
              - 'false'
            default: 'true'
        - name: full_info
          in: query
          required: false
          description: >-
            If "true", returns detailed file info; if "false", returns only the
            relative path.
          schema:
            type: string
            enum:
              - 'true'
              - 'false'
            default: 'false'
      requestBody:
        required: true
        content:
          application/octet-stream:
            schema:
              type: string
              format: binary
      responses:
        '200':
          description: File uploaded successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserDataResponseFull'
        '400':
          description: Missing or invalid 'file' parameter.
          content:
            text/plain:
              schema:
                type: string
        '401':
          description: Unauthorized.
          content:
            text/plain:
              schema:
                type: string
        '403':
          description: The requested path is not allowed.
          content:
            text/plain:
              schema:
                type: string
        '409':
          description: File already exists and overwrite is set to false.
          content:
            text/plain:
              schema:
                type: string
        '500':
          description: General error
          content:
            text/plain:
              schema:
                type: string
components:
  schemas:
    UserDataResponseFull:
      type: object
      properties:
        path:
          type: string
        size:
          type: integer
        modified:
          type: string
          format: date-time
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