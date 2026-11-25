"""Structured content constants for the Human In and PlanPaz pages."""

COMPANY_META = {
    "title": "Human In — Tecnologia para a mudança individual",
    "description": (
        "A Human In desenvolve aplicações de impacto social para colaborar no "
        "combate a problemas socioambientais por meio da mudança individual."
    ),
    "og_title": "Human In — Tecnologia para a mudança individual",
    "og_description": "Empresa brasileira de tecnologia de impacto social e criadora do PlanPaz.",
}

COMPANY_NAV = [
    {"label": "Concepção", "href": "#concepcao"},
    {"label": "Produtos", "href": "#produtos"},
    {"label": "Equipe", "href": "#equipe"},
]

COMPANY_STATS = [
    {"value": "2025", "label": "Fundação"},
    {"value": "5", "label": "Estudantes"},
    {"value": "1", "label": "Produto"},
]

CONCEPTION_CARDS = [
    {
        "title": "Quem somos",
        "text": "Cinco estudantes do IFSP São Miguel Paulista, curso de Informática para Internet (turma 2023).",
        "delay": 0,
    },
    {
        "title": "O que fazemos",
        "text": "Aplicações de impacto social contra problemas socioambientais.",
        "delay": 80,
    },
    {
        "title": "O problema",
        "text": "Tecnologia que explora a atenção em vez de resolver problemas reais.",
        "delay": 160,
    },
    {
        "title": "Como usamos tecnologia",
        "text": "Como ferramenta para formar redes em prol de causas comuns, pela participação individual.",
        "delay": 240,
    },
]

VALUES = [
    {
        "icon": "heart-handshake",
        "name": "Humanização",
        "text": "O humano faz uso da tecnologia, e não o contrário.",
    },
    {
        "icon": "lightbulb",
        "name": "Inovação",
        "text": "Criatividade para resolver problemas com tecnologia.",
    },
    {
        "icon": "feather",
        "name": "Simplicidade",
        "text": "Entregar apenas o necessário para agregar valor.",
    },
    {
        "icon": "zap",
        "name": "Eficiência",
        "text": "Soluções rápidas em cumprir seu propósito.",
    },
    {
        "icon": "sparkles",
        "name": "Colaboração",
        "text": "A realidade social muda a partir da mudança individual.",
    },
]

TEAM_MEMBERS = [
    {"index": "01", "name": "Andrew Gabriel", "role": "Scrum Master", "delay": 0},
    {"index": "02", "name": "João Manuel", "role": "Dev Backend", "delay": 90},
    {"index": "03", "name": "Leonardo Ciardi", "role": "Dev Frontend", "delay": 180},
    {"index": "04", "name": "João Paulo", "role": "Design", "delay": 270},
    {"index": "05", "name": "Matheus Pietro", "role": "Design", "delay": 360},
]

PLANPAZ_META = {
    "title": "PlanPaz — Cultive mudanças, de semente em semente",
    "description": (
        "Conheça o PlanPaz, aplicativo da Human In para identificar plantas, "
        "cuidar do seu jardim e compartilhar experiências com a comunidade."
    ),
    "og_title": "PlanPaz — Um produto Human In",
    "og_description": "O aplicativo para quem quer fazer a mudança no mundo, de semente em semente.",
}

PLANPAZ_NAV = [
    {"label": "Sobre", "href": "#sobre"},
    {"label": "Como funciona", "href": "#como-funciona"},
    {"label": "Funcionalidades", "href": "#funcionalidades"},
    {"label": "Por dentro", "href": "#por-dentro"},
    {"label": "Comunidade", "href": "#comunidade"},
]

PLANPAZ_HERO_PILLS = [
    {
        "icon": "camera",
        "text": "Planta identificada",
        "position": "-left-3 top-[14%] sm:-left-10",
        "delay": 300,
    },
    {
        "icon": "droplets",
        "text": "Regar amanhã, 8h",
        "position": "-right-3 top-[38%] sm:-right-12",
        "delay": 450,
    },
    {
        "icon": "trending-up",
        "text": "+12% de crescimento",
        "position": "-left-2 bottom-[24%] sm:-left-14",
        "delay": 600,
    },
    {
        "icon": "flower-2",
        "text": "6 plantas no jardim",
        "position": "-right-2 bottom-[6%] sm:-right-8",
        "delay": 750,
    },
]

PLANPAZ_PAINS = [
    {"text": "Não sabe qual é a espécie?", "delay": 0},
    {"text": "Esquece quando precisa regar?", "delay": 70},
    {"text": "Não sabe como cuidar?", "delay": 140},
    {"text": "Tem dúvidas sobre a saúde da planta?", "delay": 210},
    {"text": "Não tem com quem compartilhar experiências?", "delay": 280},
]

PLANPAZ_STEPS = [
    {
        "number": "01",
        "icon": "camera",
        "title": "Descubra",
        "text": "Identifique sua planta.",
        "delay": 0,
    },
    {
        "number": "02",
        "icon": "book-open",
        "title": "Entenda",
        "text": "Aprenda como cuidar dela.",
        "delay": 90,
    },
    {
        "number": "03",
        "icon": "droplets",
        "title": "Cuide",
        "text": "Receba lembretes e acompanhe seu desenvolvimento.",
        "delay": 180,
    },
    {
        "number": "04",
        "icon": "users",
        "title": "Compartilhe",
        "text": "Faça parte da comunidade.",
        "delay": 270,
    },
]

PLANPAZ_FEATURES = [
    {
        "icon": "camera",
        "title": "Identificação de plantas",
        "text": "Descubra a espécie a partir de uma foto.",
        "delay": 0,
    },
    {
        "icon": "droplets",
        "title": "Cuidados e lembretes",
        "text": "Rega e fertilização no momento certo.",
        "delay": 60,
    },
    {
        "icon": "flower-2",
        "title": "Jardim pessoal",
        "text": "Todas as suas plantas em um só lugar.",
        "delay": 120,
    },
    {
        "icon": "users",
        "title": "Comunidade",
        "text": "Troque dúvidas e experiências.",
        "delay": 180,
    },
    {
        "icon": "trophy",
        "title": "Evolução e conquistas",
        "text": "Acompanhe seu progresso como cultivador.",
        "delay": 240,
    },
    {
        "icon": "book-open",
        "title": "Informações sobre espécies",
        "text": "Origem, características e necessidades.",
        "delay": 300,
    },
]

PLANPAZ_SCREENS = [
    {
        "number": "01",
        "title": "Início",
        "caption": "Clima do dia e próximos cuidados logo na abertura.",
        "image": "images/planpaz-inicio.png",
        "alt": "Tela inicial do PlanPaz com clima e próximos lembretes",
        "stagger": False,
        "delay": 0,
    },
    {
        "number": "02",
        "title": "Identificação",
        "caption": "Busque e descubra espécies com filtros simples.",
        "image": "images/planpaz-biblioteca.png",
        "alt": "Biblioteca de espécies do PlanPaz",
        "stagger": True,
        "delay": 120,
    },
    {
        "number": "03",
        "title": "Minha planta & cuidados",
        "caption": "Seu jardim organizado, com a rotina de cada planta.",
        "image": "images/planpaz-jardim.png",
        "alt": "Galeria do Meu Jardim no PlanPaz",
        "stagger": False,
        "delay": 240,
    },
    {
        "number": "04",
        "title": "Comunidade",
        "caption": "Compartilhe conquistas e tire dúvidas.",
        "image": "images/planpaz-comunidade.png",
        "alt": "Feed da comunidade do PlanPaz",
        "stagger": True,
        "delay": 360,
    },
]

PLANPAZ_EVOLUTION = [
    {"icon": "sprout", "label": "Nível", "value": "Broto · nível 3", "percent": 62},
    {
        "icon": "flame",
        "label": "Sequência de cuidados",
        "value": "12 dias seguidos",
        "percent": 80,
    },
    {"icon": "target", "label": "Meta da semana", "value": "4 de 5 regas", "percent": 80},
    {
        "icon": "trophy",
        "label": "Conquistas",
        "value": "Primeira muda · Jardim com 5 plantas",
        "percent": 45,
    },
]

PLANPAZ_COMMUNITY = [
    {
        "initials": "AN",
        "author": "Ana",
        "text": "Minha primeira muda!",
        "likes": 24,
        "replies": "6 respostas",
        "banner_class": "bg-leaf/25",
        "delay": 0,
    },
    {
        "initials": "RF",
        "author": "Rafael",
        "text": "Alguém sabe o que está acontecendo com minha planta? As folhas estão amarelando.",
        "likes": 8,
        "replies": "14 respostas",
        "banner_class": "bg-leaf/15",
        "delay": 100,
    },
    {
        "initials": "JU",
        "author": "Júlia",
        "text": "Meu jardim depois de 30 dias.",
        "likes": 51,
        "replies": "9 respostas",
        "banner_class": "bg-leaf/35",
        "delay": 200,
    },
]

PLANPAZ_IMPACTS = [
    {
        "icon": "sprout",
        "title": "Cultivo",
        "text": "Incentivar o contato cotidiano com plantas.",
        "delay": 0,
    },
    {
        "icon": "building-2",
        "title": "Mais verde",
        "text": "Estimular práticas sustentáveis em ambientes urbanos.",
        "delay": 90,
    },
    {
        "icon": "handshake",
        "title": "Comunidade",
        "text": "Conectar pessoas através do cuidado e da troca de conhecimento.",
        "delay": 180,
    },
]

PLANPAZ_DIFFERENTIALS = [
    "Identificação",
    "Informação",
    "Cuidados",
    "Lembretes",
    "Jardim pessoal",
    "Comunidade",
    "Evolução",
]
