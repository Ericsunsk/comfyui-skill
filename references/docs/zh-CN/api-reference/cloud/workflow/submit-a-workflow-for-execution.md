> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit a workflow for execution

> Submit a workflow to be executed by the backend.
The workflow is a JSON object describing the nodes and their connections.




## OpenAPI

````yaml openapi-cloud.yaml post /api/prompt
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
  /api/prompt:
    post:
      tags:
        - workflow
      summary: Submit a workflow for execution
      description: >
        Submit a workflow to be executed by the backend.

        The workflow is a JSON object describing the nodes and their
        connections.
      operationId: executePrompt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PromptRequest'
      responses:
        '200':
          description: Success - Prompt accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromptResponse'
        '400':
          description: Invalid prompt
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromptErrorResponse'
        '402':
          description: Payment required - Insufficient credits
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromptErrorResponse'
        '429':
          description: Payment required - User has not paid
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromptErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromptErrorResponse'
        '503':
          description: Service unavailable
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromptErrorResponse'
components:
  schemas:
    PromptRequest:
      type: object
      required:
        - prompt
      properties:
        prompt:
          type: object
          description: The workflow graph to execute
          additionalProperties: true
        number:
          type: number
          description: >
            Priority number for the queue (lower numbers have higher priority).

            **Note:** Accepted for ComfyUI API compatibility but **ignored** in
            cloud.

            Cloud uses its own queue management with per-user ordering and fair
            scheduling.
        front:
          type: boolean
          description: >
            If true, adds the prompt to the front of the queue.

            **Note:** Accepted for ComfyUI API compatibility but **ignored** in
            cloud.

            Cloud manages queue ordering internally based on job submission time
            and fair scheduling.
        extra_data:
          type: object
          description: Extra data to be associated with the prompt
          additionalProperties: true
        partial_execution_targets:
          type: array
          items:
            type: string
          description: List of node names to execute
    PromptResponse:
      type: object
      properties:
        prompt_id:
          type: string
          format: uuid
          description: Unique identifier for the prompt execution
        number:
          type: number
          description: Priority number in the queue
        node_errors:
          type: object
          description: Any errors in the nodes of the prompt
          additionalProperties: true
    PromptErrorResponse:
      type: object
      description: Error response for ComfyUI prompt execution.
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