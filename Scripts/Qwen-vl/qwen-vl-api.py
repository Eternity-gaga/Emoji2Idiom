from dashscope import MultiModalConversation


def call_with_local_file():
    """Sample of use local file.
       linux&mac file schema: file:///home/images/test.png
       windows file schema: file://D:/images/abc.png
    """

    local_file_path = 'file'
    example_image_1 = 'filepath'

    messages_1 = [{
        'role': 'system',
        'content': [{
            'text': ''
        }, ]
    }, {
        'role':
        'user',
        'content': [
            {
                'text': '<Prompt>'
            },
            {
                'image': local_file_path
            },
            {
                'text': '<Prompt>'
            },
            {
                'image': example_image_1
            }
        ]
    }]
    response_1 = MultiModalConversation.call(model=MultiModalConversation.Models.qwen_vl_chat_v1, messages=messages_1)
    print(response_1)



if __name__ == '__main__':
    call_with_local_file()
