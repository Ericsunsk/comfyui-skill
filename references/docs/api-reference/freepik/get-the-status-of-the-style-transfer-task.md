> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the status of the style transfer task

> Get the status of the style transfer task



## OpenAPI

````yaml https://api.comfy.org/openapi get /proxy/freepik/v1/ai/image-style-transfer/{task_id}
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/freepik/v1/ai/image-style-transfer/{task_id}:
    get:
      tags:
        - Freepik
        - Proxy
      summary: Get the status of the style transfer task
      description: Get the status of the style transfer task
      operationId: FreepikMagnificStyleTransferGetStatus
      parameters:
        - description: ID of the task
          in: path
          name: task_id
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikTaskResponse'
          description: OK - The task status is returned
        '404':
          description: Task not found
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikErrorResponse'
          description: Internal Server Error
      security:
        - BearerAuth: []
components:
  schemas:
    FreepikTaskResponse:
      properties:
        data:
          $ref: '#/components/schemas/FreepikTaskData'
      required:
        - data
      type: object
    FreepikErrorResponse:
      properties:
        error:
          type: string
        message:
          type: string
      type: object
    FreepikTaskData:
      properties:
        generated:
          description: URLs to the generated images.
          items:
            format: uri
            type: string
          type: array
        status:
          enum:
            - CREATED
            - IN_PROGRESS
            - COMPLETED
            - FAILED
          type: string
        task_id:
          example: 046b6c7f-0b8a-43b9-b35d-6489e6daee91
          format: uuid
          type: string
      type: object
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````