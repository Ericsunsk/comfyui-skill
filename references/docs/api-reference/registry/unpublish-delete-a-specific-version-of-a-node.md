> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Unpublish (delete) a specific version of a node



## OpenAPI

````yaml https://api.comfy.org/openapi delete /publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}:
    delete:
      tags:
        - Registry
      summary: Unpublish (delete) a specific version of a node
      operationId: DeleteNodeVersion
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
        - in: path
          name: versionId
          required: true
          schema:
            type: string
      responses:
        '204':
          description: Version unpublished (deleted) successfully
        '403':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Version does not belong to the publisher
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
          description: Version not found
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Version not found
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
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````