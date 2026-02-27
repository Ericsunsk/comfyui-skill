> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a publisher



## OpenAPI

````yaml https://api.comfy.org/openapi put /publishers/{publisherId}
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /publishers/{publisherId}:
    put:
      tags:
        - Registry
      summary: Update a publisher
      operationId: UpdatePublisher
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
              $ref: '#/components/schemas/Publisher'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Publisher'
          description: Publisher updated successfully
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Bad request, invalid input data
        '401':
          description: Unauthorized
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Publisher not found
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
    Publisher:
      properties:
        createdAt:
          description: The date and time the publisher was created.
          format: date-time
          type: string
        description:
          type: string
        id:
          description: >-
            The unique identifier for the publisher. It's akin to a username.
            Should be lowercase.
          type: string
        logo:
          description: URL to the publisher's logo.
          type: string
        members:
          description: A list of members in the publisher.
          items:
            $ref: '#/components/schemas/PublisherMember'
          type: array
        name:
          type: string
        source_code_repo:
          type: string
        status:
          $ref: '#/components/schemas/PublisherStatus'
        support:
          type: string
        website:
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
    PublisherMember:
      properties:
        id:
          description: The unique identifier for the publisher member.
          type: string
        role:
          description: The role of the user in the publisher.
          type: string
        user:
          $ref: '#/components/schemas/PublisherUser'
      type: object
    PublisherStatus:
      enum:
        - PublisherStatusActive
        - PublisherStatusBanned
      type: string
    PublisherUser:
      properties:
        email:
          description: The email address for this user.
          type: string
        id:
          description: The unique id for this user.
          type: string
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