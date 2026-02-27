> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve permissions the user has for a given publisher



## OpenAPI

````yaml https://api.comfy.org/openapi get /publishers/{publisherId}/permissions
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /publishers/{publisherId}/permissions:
    get:
      tags:
        - Registry
      summary: Retrieve permissions the user has for a given publisher
      operationId: GetPermissionOnPublisher
      parameters:
        - in: path
          name: publisherId
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                properties:
                  canEdit:
                    type: boolean
                type: object
          description: A list of permissions
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Bad request, invalid input data
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Internal server error
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

````