> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get system statistics

> Returns system statistics including ComfyUI version, device info, and system resources



## OpenAPI

````yaml openapi-cloud.yaml get /api/system_stats
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
  /api/system_stats:
    get:
      tags:
        - system
      summary: Get system statistics
      description: >-
        Returns system statistics including ComfyUI version, device info, and
        system resources
      operationId: getSystemStats
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SystemStatsResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security: []
components:
  schemas:
    SystemStatsResponse:
      type: object
      description: System statistics response
      required:
        - system
        - devices
      properties:
        system:
          type: object
          required:
            - os
            - python_version
            - embedded_python
            - comfyui_version
            - pytorch_version
            - argv
            - ram_total
            - ram_free
          properties:
            os:
              type: string
              description: Operating system
            python_version:
              type: string
              description: Python version
            embedded_python:
              type: boolean
              description: Whether using embedded Python
            comfyui_version:
              type: string
              description: ComfyUI version
            comfyui_frontend_version:
              type: string
              description: ComfyUI frontend version (commit hash or tag)
            workflow_templates_version:
              type: string
              description: Workflow templates version
            cloud_version:
              type: string
              description: Cloud ingest service version (commit hash)
            pytorch_version:
              type: string
              description: PyTorch version
            argv:
              type: array
              items:
                type: string
              description: Command line arguments
            ram_total:
              type: number
              description: Total RAM in bytes
            ram_free:
              type: number
              description: Free RAM in bytes
        devices:
          type: array
          items:
            type: object
            required:
              - name
              - type
            properties:
              name:
                type: string
                description: Device name
              type:
                type: string
                description: Device type
              vram_total:
                type: number
                description: Total VRAM in bytes
              vram_free:
                type: number
                description: Free VRAM in bytes
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