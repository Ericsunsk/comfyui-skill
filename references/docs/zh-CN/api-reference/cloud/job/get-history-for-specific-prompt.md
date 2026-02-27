> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get history for specific prompt

> Retrieve detailed execution history for a specific prompt ID.
Returns full history data including complete prompt information.




## OpenAPI

````yaml openapi-cloud.yaml get /api/history_v2/{prompt_id}
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
  /api/history_v2/{prompt_id}:
    get:
      tags:
        - job
      summary: Get history for specific prompt
      description: |
        Retrieve detailed execution history for a specific prompt ID.
        Returns full history data including complete prompt information.
      operationId: getHistoryForPrompt
      parameters:
        - name: prompt_id
          in: path
          required: true
          description: The prompt ID to retrieve history for
          schema:
            type: string
      responses:
        '200':
          description: Success - History for prompt retrieved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HistoryDetailResponse'
        '401':
          description: Unauthorized - Authentication required
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Prompt not found
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
    HistoryDetailResponse:
      type: object
      description: >
        Detailed execution history response for a specific prompt.

        Returns a dictionary with prompt_id as key and full history data as
        value.
      additionalProperties:
        $ref: '#/components/schemas/HistoryDetailEntry'
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
    HistoryDetailEntry:
      type: object
      description: History entry with full prompt data
      properties:
        prompt:
          type: object
          description: Full prompt execution data
          properties:
            priority:
              type: number
              format: double
              description: Execution priority
            prompt_id:
              type: string
              description: The prompt ID
            prompt:
              type: object
              description: The workflow nodes
              additionalProperties: true
            extra_data:
              type: object
              description: Additional execution data
              additionalProperties: true
            outputs_to_execute:
              type: array
              items:
                type: string
              description: Output nodes to execute
        outputs:
          type: object
          description: Output data from execution (generated images, files, etc.)
          additionalProperties: true
        status:
          type: object
          description: Execution status and timeline information
          additionalProperties: true
        meta:
          type: object
          description: Metadata about the execution and nodes
          additionalProperties: true
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