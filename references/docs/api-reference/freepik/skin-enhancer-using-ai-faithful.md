> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Skin enhancer using AI (Faithful)

> Enhance skin in images using AI with the Faithful mode. This mode preserves the original appearance while improving skin quality.



## OpenAPI

````yaml https://api.comfy.org/openapi post /proxy/freepik/v1/ai/skin-enhancer/faithful
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/freepik/v1/ai/skin-enhancer/faithful:
    post:
      tags:
        - Freepik
        - Proxy
      summary: Skin enhancer using AI (Faithful)
      description: >-
        Enhance skin in images using AI with the Faithful mode. This mode
        preserves the original appearance while improving skin quality.
      operationId: FreepikSkinEnhancerFaithful
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FreepikSkinEnhancerFaithfulRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikTaskResponse'
          description: OK - The skin enhancer process has started
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikErrorResponse'
          description: Bad Request
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikErrorResponse'
          description: Internal Server Error
      security:
        - BearerAuth: []
components:
  schemas:
    FreepikSkinEnhancerFaithfulRequest:
      properties:
        image:
          description: >-
            Input image. Supports Base64 encoding or HTTPS URL (must be publicly
            accessible).
          example: https://example.com/portrait.jpg
          type: string
        sharpen:
          default: 0
          description: Sharpening intensity
          maximum: 100
          minimum: 0
          type: integer
        skin_detail:
          default: 80
          description: Skin detail enhancement level
          maximum: 100
          minimum: 0
          type: integer
        smart_grain:
          default: 2
          description: Smart grain intensity
          maximum: 100
          minimum: 0
          type: integer
        webhook_url:
          description: Optional callback URL for async notifications.
          example: https://www.example.com/webhook
          format: uri
          type: string
      required:
        - image
      type: object
    FreepikTaskResponse:
      properties:
        data:
          $ref: '#/components/schemas/FreepikTaskData'
      required:
        - data
      type: object
    FreepikErrorResponse:
      properties:
        error:
          type: string
        message:
          type: string
      type: object
    FreepikTaskData:
      properties:
        generated:
          description: URLs to the generated images.
          items:
            format: uri
            type: string
          type: array
        status:
          enum:
            - CREATED
            - IN_PROGRESS
            - COMPLETED
            - FAILED
          type: string
        task_id:
          example: 046b6c7f-0b8a-43b9-b35d-6489e6daee91
          format: uuid
          type: string
      type: object
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````