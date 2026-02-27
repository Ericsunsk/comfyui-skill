> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Validate if a publisher username is available

> Checks if the publisher username is already taken.



## OpenAPI

````yaml https://api.comfy.org/openapi get /publishers/validate
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /publishers/validate:
    get:
      tags:
        - Registry
      summary: Validate if a publisher username is available
      description: Checks if the publisher username is already taken.
      operationId: ValidatePublisher
      parameters:
        - description: The publisher username to validate.
          in: query
          name: username
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                properties:
                  isAvailable:
                    description: True if the username is available, false otherwise.
                    type: boolean
                type: object
          description: Username validation result
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Invalid input, such as missing username in the query.
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