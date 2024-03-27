from openai import OpenAI
import os
import time

client = OpenAI()



# List mdx files in current folder
mdx_filenames = [f for f in os.listdir() if f.endswith('.mdx')]
mdx_filenames = sorted(mdx_filenames)

# Read the content of each mdx file
mdx_contents = dict()
for filename in mdx_filenames:
    with open(filename, 'r') as f:
        mdx_contents[filename] = f.read()

OUTLINE = """
Context: we are making a tutorial that builds up to the ChatGpt.sol contract step by step, explaining why each part of the code is necessary as we add it.

* Make sure you have a wallet. Get devnet tokens from faucet. (just link to wallet and faucet pages, no need to explain detailed steps)
* Clone the repo and install dependencies. Start the local node.
* Create a new trivial contract
* add oracle address in contract constructor, and an oracle address setter function and the modifier onlyOwner. Explain that oracle address may occasionally change, which is why this is needed.
* create function startChat, empty for now
* add struct Message and ChatRun
* add oracle interface to contract, and createLlmCall into startChat
* add getMessageHistoryContents and getMessageHistoryRoles
* add onOracleLlmResponse, empty at first
* script to deploy the contract
* deploy contract
* see in explorer
* script to call the contract
* call contract
* see result in explorer
* what next: see reference & how it works
"""

messages = [
    {
        "role": "system",
        "content": """You are a tutorial writer. Your purpose is to write a tutorial from the given outline provided by the user, using as context the content of the mdx files provided.
        
        The tutorial should be written in MDX format compatible with Mintlify, but just output MDX content without '```mdx' tags.

        Don't copy much content from other pages; instead refer to them in a link (e.g. to link to "about.mdx", use [About](/about.mdx)).

        In every step of the tutorial, be verbose with code examples, bash commands to run, etc. Expand the given outline to be maximally helpful for a user new to the product.
        """
    },
    {
        "role": "user",
        "content": f"Please write a tutorial based on the following outline:\n{OUTLINE}"
    }
]

for filename in mdx_filenames:
    messages.append({
        "role": "user",
        "content": f"=== Contents of {filename}===\n{mdx_contents[filename]}\n\n\ns"
    })

with open("/Users/taivo/galadriel/contracts/contracts/contracts/ChatGpt.sol") as f:
    contract_contents = f.read()
messages.append({
    "role": "user",
    "content": f"=== Contents of ChatGpt.sol ===\n{contract_contents}"
})

print(f"Created context, {len(messages)} messages, sending to OpenAI")

start_time = time.time()
completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=messages
)

end_time = time.time()
total_sec = end_time - start_time
total_tok = completion.usage.completion_tokens
ms_per_token = 1000. * total_sec / total_tok

print(f"Received response from OpenAI")
print(f"\n\t{total_tok} tokens produced\n\t")
print(f"Total time taken: {total_sec:.0f} seconds, {ms_per_token:.0f} ms per token")

result_mdx = completion.choices[0].message.content

with open("tutorials/tutorial.mdx", "w") as f:
    f.write(result_mdx)
