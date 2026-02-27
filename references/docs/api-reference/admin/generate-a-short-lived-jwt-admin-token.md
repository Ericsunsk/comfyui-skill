> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate a short-lived JWT admin token

> Generates a short-lived JWT admin token for browser-based admin operations.
The user must already be authenticated with Firebase and have admin privileges.
The generated token expires after 1 hour.




## OpenAPI

````yaml https://api.comfy.org/openapi post /admin/generate-token
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /admin/generate-token:
    post:
      tags:
        - Admin
      summary: Generate a short-lived JWT admin token
      description: >
        Generates a short-lived JWT admin token for browser-based admin
        operations.

        The user must already be authenticated with Firebase and have admin
        privileges.

        The generated token expires after 1 hour.
      operationId: GenerateAdminToken
      responses:
        '200':
          content:
            application/json:
              schema:
                properties:
                  expires_at:
                    description: When the token expires
                    format: date-time
                    type: string
                  token:
                    description: The JWT admin token
                    type: string
                required:
                  - token
                  - expires_at
                type: object
          description: JWT token generated successfully
        '401':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Unauthorized or user is not an admin
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