> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a specific node



## OpenAPI

````yaml https://api.comfy.org/openapi delete /publishers/{publisherId}/nodes/{nodeId}
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /publishers/{publisherId}/nodes/{nodeId}:
    delete:
      tags:
        - Registry
      summary: Delete a specific node
      operationId: DeleteNode
      parameters:
        - in: path
          name: publisherId
          required: true
          schema:
            type: string
        - in: path
          name: nodeId
          required: true
          schema:
            type: string
      responses:
        '204':
          description: Node deleted successfully
        '403':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Forbidden
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Node not found
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Internal server error
      security:
        - BearerAuth: []
components:
  schemas:
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
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````