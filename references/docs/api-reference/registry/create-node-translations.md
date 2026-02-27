> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Node Translations



## OpenAPI

````yaml https://api.comfy.org/openapi post /nodes/{nodeId}/translations
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /nodes/{nodeId}/translations:
    post:
      tags:
        - Registry
      summary: Create Node Translations
      operationId: CreateNodeTranslations
      parameters:
        - description: The unique identifier of the node.
          in: path
          name: nodeId
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              properties:
                data:
                  additionalProperties:
                    additionalProperties: true
                    type: object
                  type: object
              type: object
        required: true
      responses:
        '201':
          description: Detailed information about a specific node
        '400':
          description: Bad Request
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
          description: Node version not found
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Internal server error
components:
  schemas:
    Error:
      properties:
        details:
          description: >-
            Optional detailed information about the error or hints for resolving
            it.
          items:
            type: string
          type: array
        message:
          description: A clear and concise description of the error.
          type: string
      type: object
    ErrorResponse:
      properties:
        error:
          type: string
        message:
          type: string
      required:
        - error
        - message
      type: object

````