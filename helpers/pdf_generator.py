from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Ion by Liviu Rebreanu: An In-depth Summary', 0, 1, 'C')
        self.ln(10)
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()
    
    def add_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

pdf = PDF()
pdf.set_left_margin(10)
pdf.set_right_margin(10)
pdf.add_page()

introduction = (
    "'Ion,' authored by Liviu Rebreanu and first published in 1920, stands as a monumental work in Romanian literature. "
    "Set against the backdrop of rural Transylvania, the novel intricately weaves the socio-economic struggles and moral dilemmas "
    "of the peasantry into its narrative. The story primarily follows the life of Ion, a poor but ambitious peasant, whose relentless "
    "quest for land and social status drives the plot. Through vivid character portrayals and a detailed depiction of village life, "
    "Rebreanu creates a compelling tale of ambition, love, and tragedy.\n\n"
)

setting_characters = (
    "The novel is set in the village of Pripas, a microcosm of rural Transylvania. The environment is described with meticulous detail, "
    "capturing the essence of village life, its rhythms, and its inherent struggles.\n\n"
    "Main Characters:\n\n"
    "- Ion Popescu (Ion al Glanetasului): The protagonist, a hardworking and determined young peasant whose primary ambition is to acquire land and elevate his social status.\n"
    "- Ana Baciu: The daughter of Vasile Baciu, a wealthy landowner. She becomes Ion's wife, though her life is marked by suffering and tragedy.\n"
    "- Vasile Baciu: Ana's father, a protective and controlling landowner who initially opposes Ion's courtship of Ana.\n"
    "- Vanessa: Ion's true love, a beautiful but impoverished girl who symbolizes unattainable love for Ion.\n"
    "- George Bulbuc: A wealthy but lazy suitor of Ana, representing the idle rich.\n"
    "- Titu Herdelea: A young intellectual and friend of Ion, providing a contrast to Ion's peasant ambitions.\n\n"
)

plot_overview = (
    "Ion's Ambition\n"
    "The story begins with Ion's life as a poor peasant, deeply infatuated with Vanessa but keenly aware of his poverty. His ambition to acquire land and improve his social standing becomes an all-consuming obsession. Ion recognizes that marrying Ana, who possesses a considerable dowry in the form of land, is his quickest path to achieving his dreams.\n\n"
    "Courtship and Conflict\n"
    "Ion's pursuit of Ana is marked by strategic charm and manipulation. He wins Ana's affection despite her father Vasile Baciu's disapproval. Baciu, aware of Ion's motives, tries to marry Ana off to George Bulbuc, a more suitable match in his eyes due to his wealth. However, Ana, driven by her love for Ion, resists her father's plans.\n\n"
    "Marriage and Tragedy\n"
    "Ion's relentless pursuit culminates in his marriage to Ana. However, the marriage is fraught with unhappiness. Ion's indifference and harsh treatment of Ana, coupled with his obsession with the newly acquired land, lead to a tragic decline in Ana's well-being. Ana's depression deepens, and she eventually dies in childbirth, leaving Ion with their infant son. This event marks a turning point, highlighting the personal cost of Ion's ambitions.\n\n"
    "Consequences and Downfall\n"
    "Ana's death sets off a chain of events leading to Ion's downfall. His greed and ruthless ambition alienate him from the community. Vanessa, now married to another man, remains a symbol of unattainable love and happiness for Ion. His relentless pursuit of wealth and social status ultimately leads to his tragic end. In a dramatic climax, Ion is murdered by George Bulbuc in a fit of jealousy and revenge, bringing his ambitions and life to a tragic close.\n\n"
)

themes_analysis = (
    "The Struggle for Land\n"
    "Land in 'Ion' is a powerful symbol of wealth, power, and social status. Ion's obsession with acquiring land reflects the broader socio-economic struggles of the peasantry in rural Transylvania. This struggle underscores the novel's exploration of class and economic disparity.\n\n"
    "Social and Economic Inequality\n"
    "Rebreanu provides a critical portrayal of class divisions and economic disparities. Vasile Baciu's wealth and influence starkly contrast with the poverty and powerlessness of characters like Ion and Vanessa. This dynamic illuminates the harsh realities of rural life and the limited opportunities for social mobility.\n\n"
    "Ambition and Morality\n"
    "Ion's character embodies the complex interplay between ambition and morality. His ruthless pursuit of land and social status leads to morally questionable decisions, culminating in his tragic downfall. The novel questions the ethical boundaries of ambition and the human cost of unrestrained desire for advancement.\n\n"
    "Love and Sacrifice\n"
    "Through the relationships between the characters, the novel delves into themes of love and sacrifice. Ana's love for Ion and her subsequent suffering highlight the personal costs of Ion's ambition. Vanessa's unattainable love for Ion adds another layer of complexity to his character, symbolizing the sacrifices and unfulfilled desires inherent in the pursuit of ambition.\n\n"
    "The Role of Women\n"
    "'Ion' examines the role of women in rural society, particularly through the characters of Ana and Vanessa. 'Ana's tragic fate underscores the limited agency and harsh treatment of women in a patriarchal social structure. The novel critiques the societal norms that confine and oppress women, portraying their struggles with empathy and depth.\n\n"
)

conclusion = (
    "'Ion' by Liviu Rebreanu is a profound exploration of the human condition set against the backdrop of rural Transylvania. Through its intricate narrative and complex characters, the novel delves into themes of ambition, social inequality, and moral dilemmas. Ion's tragic journey from a poor peasant to a landowner and his ultimate downfall serves as a poignant commentary on the costs of unchecked ambition and the enduring struggles of the rural peasantry. Rebreanu's masterful storytelling and keen social insight make 'Ion' a timeless work that continues to resonate with readers.\n\n"
)

pdf.add_chapter('Introduction', introduction)
pdf.add_chapter('Setting and Characters', setting_characters)
pdf.add_chapter('Plot Overview', plot_overview)
pdf.add_chapter('Themes and Analysis', themes_analysis)
pdf.add_chapter('Conclusion', conclusion)

# Save the PDF
pdf_output_path = "../data/ion-resume.pdf"
pdf.output(pdf_output_path)

pdf_output_path
