> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Claim nodeId into publisherId for the authenticated publisher

> This endpoint allows a publisher to claim an unclaimed node that they own the repo, which is identified by the nodeId. The unclaimed node's repository must be owned by the authenticated user.




## OpenAPI

````yaml https://api.comfy.org/openapi post /publishers/{publisherId}/nodes/{nodeId}/claim-my-node
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /publishers/{publisherId}/nodes/{nodeId}/claim-my-node:
    post:
      tags:
        - Registry
      summary: Claim nodeId into publisherId for the authenticated publisher
      description: >
        This endpoint allows a publisher to claim an unclaimed node that they
        own the repo, which is identified by the nodeId. The unclaimed node's
        repository must be owned by the authenticated user.
      operationId: ClaimMyNode
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ClaimMyNodeRequest'
        required: true
      responses:
        '204':
          description: Node claimed successfully
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Bad request, invalid input data
        '401':
          description: Unauthorized
        '403':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: |
            Forbidden - various authorization and permission issues
            Includes:
            - The authenticated user does not have permission to claim the node
            - The node is already claimed by another publisher
            - The GH_TOKEN is invalid
            - The repository is not owned by the authenticated GitHub user
        '429':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Too many requests - GitHub API rate limit exceeded
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Internal server error
        '503':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Service unavailable - GitHub API is currently unavailable
      security:
        - BearerAuth: []
components:
  schemas:
    ClaimMyNodeRequest:
      properties:
        GH_TOKEN:
          description: GitHub token to verify if the user owns the repo of the node
          type: string
      required:
        - GH_TOKEN
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