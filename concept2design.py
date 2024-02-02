import requests
import json
import re
import os
def node2design(base_concept, additive_concept):
    COMPLETION_URL = "https://api.openai.com/v1/chat/completions"
    API_KEY = os.environ.get("OPENAI_API_KEY")
    headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}",
            }
    inspiration_prompt = """
    Base Concept: drying rack
    Additive Concept: tree
    Explanation: Inspired by the shape of a tree, the rack is designed as a trunk and several branches, which can be used to hang objects. At the same time, the tree also has natural antibacterial and waterproof properties.
    Description: organicKidz Baby Bottle Tree is a sustainable baby bottle drying rack made from solid bamboo. The Baby Bottle Tree will not leach toxins like plastic racks. Renewable bamboo was selected due to its bacteria resistant and water repellent properties. The form is inspired by a natural tree shape and eliminates water pooling and prevents minerals and bacteria from building up. The Baby Bottle Tree design utilizes minimal counter space, has scratch-proof rubber feet and is compatible with all bottles. The tree can be repurposed as a jewellery stand or key holder.
    Base Concept: LED
    Additive Concept: candle
    Explanation: Inspired by the warm feeling that candles give, the LED lens can try to imitate the shape of a candle's candle flame, thus giving an elegant, warm and inviting feeling of being illuminated with candles.
    Description: This high-quality LED candle lamp series for chandeliers was especially designed to create an elegant lighting atmosphere in hospitality and retail environments. An innovative lens design allows a unique range of LED lamps with a pleasantly warm, sparkling light. The candle lamps create incandescent-like, dazzling light effects for a pleasing ambience and guarantee uniform light distribution.
    Base Concept: tap
    Additive Concept: seesaw
    Explanation: Inspired by the principle that a seesaw can change its balance direction by changing the force at one end, a tap with the same principle as a seesaw can be designed, allowing the user to control the opening and closing of the tap by the gravity of the cup alone, eliminating the need to touch the tap with the hand.
    Description: This purist water dispensing tap functions on the principle of a seesaw and makes use of the lever principle to fill glasses or cups. The weight of the vessel activates the water flow, removing it stops the water flow automatically. By this means, the user always has one hand free, since he no longer needs to operate a lever, thus making the tap particularly hygienic. The tap is made of high-quality lead-free brass and stainless steel.
    """
    # base_concept = "cup"
    # additive_concept = "kangaroo"
    inspiration_prompt += "Base Concept: "+base_concept+"\nAdditive Concept: "+additive_concept
    print("Base Concept: "+base_concept+"\nAdditive Concept: "+additive_concept)

    history = [{'role': 'user', 'content': inspiration_prompt}]
    payload = {
                "model": "gpt-3.5-turbo",
                "messages": history,
                "temperature": 1.0,
                "top_p": 1.0,
                "n": 1,
                "stream": False,
                "presence_penalty": 0,
                "frequency_penalty": 0,
            }
    response = requests.post(
                        COMPLETION_URL,
                        headers=headers,
                        json=payload,
                        stream=False,
                        timeout=60,
                    )
    # print(response.content)
    # c = {"id":"chatcmpl-QXlha2FBbmROaXhpZUFyZUF3ZXNvbWUK","object":"chat.completion","created":0,"model":"gpt-3.5-turbo-0301","usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0},"choices":[{"index":0,"message":{"role":"assistant","content":"你好！有什么我可以帮你的吗？"},"finish_reason":"stop"}]}
    c = json.loads(response.content.decode('utf8'))
    print(c["choices"][0]["message"]["content"])
    text = c["choices"][0]["message"]["content"]
    explanation = re.search(r'Explanation: (.+?)\n', text).group(1)
    description = re.search(r'Description: (.+)', text).group(1)
    content = {"explanation":explanation,"description":description}
    return json.dumps(content)