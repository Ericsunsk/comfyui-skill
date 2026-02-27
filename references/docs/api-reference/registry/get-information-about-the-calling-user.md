> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get information about the calling user.



## OpenAPI

````yaml https://api.comfy.org/openapi get /users
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /users:
    get:
      tags:
        - Registry
      summary: Get information about the calling user.
      operationId: GetUser
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: OK
        '401':
          description: Unauthorized
        '404':
          description: Not Found
      security:
        - BearerAuth: []
components:
  schemas:
    User:
      properties:
        email:
          description: The email address for this user.
          type: string
        id:
          description: The unique id for this user.
          type: string
        isAdmin:
          description: Indicates if the user has admin privileges.
          type: boolean
        isApproved:
          description: Indicates if the user is approved.
          type: boolean
        name:
          description: The name for this user.
          type: string
      type: object
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````