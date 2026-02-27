> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new personal access token



## OpenAPI

````yaml https://api.comfy.org/openapi post /publishers/{publisherId}/tokens
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /publishers/{publisherId}/tokens:
    post:
      tags:
        - Registry
      summary: Create a new personal access token
      operationId: CreatePersonalAccessToken
      parameters:
        - in: path
          name: publisherId
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PersonalAccessToken'
        required: true
      responses:
        '201':
          content:
            application/json:
              schema:
                properties:
                  token:
                    description: The newly created personal access token.
                    type: string
                type: object
          description: Token created successfully
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Bad request, invalid input data.
        '403':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Forbidden
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
    PersonalAccessToken:
      properties:
        createdAt:
          description: '[Output Only]The date and time the token was created.'
          format: date-time
          type: string
        description:
          description: Optional. A more detailed description of the token's intended use.
          type: string
        id:
          description: Unique identifier for the GitCommit
          format: uuid
          type: string
        name:
          description: Required. The name of the token. Can be a simple description.
          type: string
        token:
          description: >-
            [Output Only]. The personal access token. Only returned during
            creation.
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
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````