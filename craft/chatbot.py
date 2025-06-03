from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hi there! I’m your Craft Idea Bot. Need a craft idea?"]
    ],
    [
        r"paper craft",
        ["Try paper flowers, greeting cards, or origami animals."]
    ],
    [
        r"cloth craft",
        ["Try making pouches, hand-stitched toys, or cloth flowers."]
    ],
    [
        r"wool craft",
        ["Try finger knitting or making pom-poms and wall hangings."]
    ],
    [
        r"easy craft",
        ["Make bookmarks, paper fans, or button art."]
    ],
    [
        r"fun craft",
        ["Try slime making, rock painting, or balloon animals."]
    ],
    [
        r"craft for kids",
        ["Kids can make masks, paper chains, or popsicle stick puppets."]
    ],
    [
        r"craft for children",
        ["How about sock puppets, paper hats, or painting stones?"]
    ],
    [
        r"craft for school",
        ["Make chart-based crafts, 3D models, or DIY pencil holders."]
    ],
    [
        r"craft for teens",
        ["Teens might like resin keychains, scrapbooks, or DIY jewelry."]
    ],
    [
        r"craft for adults",
        ["Adults can try canvas painting, embroidery, or home decor DIYs."]
    ],
    [
        r"craft for (.*)",
        ["Some great ideas for \1 are DIY cards, handmade gifts, or recycled decorations."]
    ],
    [
        r"gift for (.*)",
        ["A handmade gift for \1 could be a personalized card, photo frame, or keychain."]
    ],
    [
        r"craft for (.*) year old",
        ["For a \1 year old, try safe and fun crafts like finger painting or paper folding."]
    ],
    [
        r"(.*) decoration",
        ["For \1 decoration, try making garlands, wall hangings, or table centerpieces."]
    ],
    [
        r"how to make (.*)",
        ["To make \1, you'll need basic materials like glue, paper, scissors, and creativity!"]
    ],
    [
        r"what to make with (.*)",
        ["With \1, you can create fun crafts like organizers, toys, or decorative items."]
    ],
    [
        r"idea with (.*)",
        ["You can use \1 to make unique craft items. Try searching online for inspiration."]
    ],
    [
        r"i want to make (.*)",
        ["That’s great! Making \1 can be fun. Gather your supplies and start crafting!"]
    ],
    [
        r"(.*) idea",
        ["You could try a DIY project based on \1 using simple materials like paper and glue."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! Let your creativity shine!"]
    ],
    [
        r"quit",
        ["Goodbye! Happy crafting!"]
    ],
    [
        r"(.*)",
        ["Hmm, I didn’t get that. Try asking for craft ideas with a material, occasion, or age group."]
    ]
]


# Run chatbot
print("Hi! I’m your Craft Idea Bot. Ask me for craft ideas. Type 'quit' to exit.")
chat = Chat(pairs, reflections)
chat.converse()