> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# List all tags

> Retrieves a list of all tags used across assets.
Includes usage counts and filtering options.




## OpenAPI

````yaml openapi-cloud.yaml get /api/tags
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
  /api/tags:
    get:
      tags:
        - asset
      summary: List all tags
      description: |
        Retrieves a list of all tags used across assets.
        Includes usage counts and filtering options.
      operationId: listTags
      parameters:
        - name: prefix
          in: query
          description: Filter tags by prefix
          schema:
            type: string
        - name: limit
          in: query
          description: Maximum number of tags to return (1-1000)
          schema:
            type: integer
            minimum: 1
            maximum: 1000
            default: 100
        - name: offset
          in: query
          description: Number of tags to skip for pagination
          schema:
            type: integer
            minimum: 0
            default: 0
        - name: order
          in: query
          description: Sort order for tags
          schema:
            type: string
            enum:
              - count_desc
              - name_asc
            default: count_desc
        - name: include_zero
          in: query
          description: Include tags with zero usage count
          schema:
            type: boolean
            default: false
        - name: include_public
          in: query
          description: Whether to include public/shared assets when counting tags
          schema:
            type: boolean
            default: true
      responses:
        '200':
          description: Tags retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListTagsResponse'
        '400':
          description: Invalid request parameters
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
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    ListTagsResponse:
      type: object
      required:
        - tags
        - total
        - has_more
      properties:
        tags:
          type: array
          items:
            $ref: '#/components/schemas/TagInfo'
          description: List of tags
        total:
          type: integer
          description: Total number of tags
        has_more:
          type: boolean
          description: Whether more tags are available
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
    TagInfo:
      type: object
      required:
        - name
        - count
      properties:
        name:
          type: string
          description: Tag name
        count:
          type: integer
          description: Number of assets using this tag
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