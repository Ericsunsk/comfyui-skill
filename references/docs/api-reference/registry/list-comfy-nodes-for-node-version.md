> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# list comfy-nodes for node version



## OpenAPI

````yaml https://api.comfy.org/openapi get /nodes/{nodeId}/versions/{version}/comfy-nodes
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /nodes/{nodeId}/versions/{version}/comfy-nodes:
    parameters:
      - in: path
        name: nodeId
        required: true
        schema:
          type: string
      - in: path
        name: version
        required: true
        schema:
          type: string
    get:
      tags:
        - Registry
      summary: list comfy-nodes for node version
      operationId: ListComfyNodes
      parameters:
        - description: The page number to retrieve.
          in: query
          name: page
          schema:
            default: 1
            type: integer
        - description: The number of items to include per page.
          in: query
          name: limit
          schema:
            default: 10
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                properties:
                  comfy_nodes:
                    items:
                      $ref: '#/components/schemas/ComfyNode'
                    type: array
                  totalNumberOfPages:
                    type: integer
                type: object
          description: Comy Nodes obtained successfully
        '401':
          description: Unauthorized
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
          description: Version not found
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Internal server error
components:
  schemas:
    ComfyNode:
      properties:
        category:
          description: UI category where the node is listed, used for grouping nodes.
          type: string
        comfy_node_name:
          description: Unique identifier for the node
          type: string
        deprecated:
          description: >-
            Indicates if the node is deprecated. Deprecated nodes are hidden in
            the UI.
          type: boolean
        description:
          description: Brief description of the node's functionality or purpose.
          type: string
        experimental:
          description: >-
            Indicates if the node is experimental, subject to changes or
            removal.
          type: boolean
        function:
          description: Name of the entry-point function to execute the node.
          type: string
        input_types:
          description: Defines input parameters
          type: string
        output_is_list:
          description: Boolean values indicating if each output is a list.
          items:
            type: boolean
          type: array
        policy:
          $ref: '#/components/schemas/ComfyNodePolicy'
        return_names:
          description: Names of the outputs for clarity in workflows.
          type: string
        return_types:
          description: Specifies the types of outputs produced by the node.
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
    ComfyNodePolicy:
      enum:
        - ComfyNodePolicyActive
        - ComfyNodePolicyBanned
        - ComfyNodePolicyLocalOnly
      type: string

````