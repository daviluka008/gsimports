import streamlit as st
import os
from PIL import Image

# =============================================
# CONFIGURAÇÕES
# =============================================
WHATSAPP_NUMBER = "5511991887510"
INSTAGRAM_URL = "https://www.instagram.com/gsimports.sp"
WHATSAPP_BASE = "https://wa.me/" + WHATSAPP_NUMBER

# =============================================
# PRODUTOS
# =============================================
PRODUCTS = [
    {"id":1,  "name":"Camisa Brasil Amarela",        "brand":"Seleção Brasileira","category":"Seleções",             "description":"Modelo amarelo. Vista as cores do Brasil com orgulho.",         "sizes":"P / M / G / GG", "price":"Consultar","badge":"🆕 NOVO","image":"camisa_brasil_amarela.jpeg"},
    {"id":2,  "name":"Camisa Brasil Azul",           "brand":"Seleção Brasileira","category":"Seleções",             "description":"Modelo azul alternativo. Para os verdadeiros torcedores.",      "sizes":"P / M / G / GG", "price":"Consultar","badge":"🆕 NOVO","image":"camisa_brasil_azul.jpeg"},
    {"id":3,  "name":"Moletom Fear of God — Marrom", "brand":"Fear of God",       "category":"Moletons",             "description":"Tecido pesado, acabamento impecável e estilo único streetwear.", "sizes":"M / G / GG", "price":"R$ 150,00", "badge":"",        "image":"nevoa_marrom.jpeg"},
    {"id":4,  "name":"Moletom Fear of God — Preto",  "brand":"Fear of God",       "category":"Moletons",             "description":"Corte oversized, tecido premium e visual minimalista.",          "sizes":"M / G / GG", "price":"R$ 150,00", "badge":"",        "image":"frente_fog_preto.jpg"},
    {"id":5,  "name":"Moletom Fear of God — Azul",   "brand":"Fear of God",       "category":"Moletons",             "description":"Peça exclusiva com acabamento de alto padrão.",                  "sizes":"M / G / GG", "price":"R$ 150,00", "badge":"",        "image":"frente_fog_azul.jpeg"},
    {"id":6,  "name":"Moletom Fear of God — Branco", "brand":"Fear of God",       "category":"Moletons",             "description":"Clássico e versátil, ideal para qualquer ocasião.",              "sizes":"M / G / GG", "price":"R$ 150,00", "badge":"",        "image":"frente_fog_branco.jpeg"},
    {"id":7,  "name":"Moletom Fear of God — Cinza",  "brand":"Fear of God",       "category":"Moletons",             "description":"Streetwear premium no seu melhor.",                              "sizes":"M / G / GG", "price":"R$ 150,00", "badge":"",        "image":"frente_fog_cinza.jpeg"},
    {"id":8,  "name":"Moletom Nike — Branco",        "brand":"Nike",              "category":"Moletons",             "description":"Tecido de alta qualidade, corte moderno e conforto garantido.",  "sizes":"M / G / GG", "price":"R$ 150,00", "badge":"",        "image":"frente_nike_branca.jpeg"},
    {"id":9,  "name":"Moletom Nike — Cinza",         "brand":"Nike",              "category":"Moletons",             "description":"O clássico Nike com acabamento premium.",                        "sizes":"M / G / GG", "price":"R$ 150,00", "badge":"",        "image":"frente_nike_cinza.jpeg"},
    {"id":10, "name":"Moletom Nike — Preto",         "brand":"Nike",              "category":"Moletons",             "description":"Estilo e conforto em uma peça essencial.",                       "sizes":"M / G / GG", "price":"R$ 150,00", "badge":"",        "image":"frente_nike_preto.jpeg"},
    {"id":11, "name":"Camisetas Boss",               "brand":"Boss",              "category":"Camisetas Tradicionais","description":"Sofisticação e estilo europeu em cada detalhe.",                "sizes":"P / M / G / GG", "price":"Consultar","badge":"",     "image":"camisetas_boss.jpeg"},
    {"id":12, "name":"Camisetas Tommy Hilfiger",     "brand":"Tommy Hilfiger",    "category":"Camisetas Tradicionais","description":"Clássico americano com acabamento premium.",                    "sizes":"P / M / G / GG", "price":"Consultar","badge":"",     "image":"camisetas_tommy.jpeg"},
]

CATEGORIES = ["Todos"] + sorted(set(p["category"] for p in PRODUCTS))
BRANDS    = ["Todas"]  + sorted(set(p["brand"]    for p in PRODUCTS))

# =============================================
# CSS mínimo — só estilo geral, sem cards em HTML
# =============================================
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;600;700&display=swap');

    .stApp { background:#0a0a0a; color:#f0f0f0; font-family:'Inter',sans-serif; }
    #MainMenu, footer, header { visibility:hidden; }
    .block-container { padding-top:0 !important; padding-bottom:0 !important; max-width:100% !important; }

    /* Navbar */
    .gs-navbar {
        background:#0d0d0d; border-bottom:1px solid #222;
        padding:16px 40px; display:flex; align-items:center;
        justify-content:space-between;
    }
    .gs-logo { font-family:'Bebas Neue',sans-serif; font-size:1.9rem; letter-spacing:5px; color:#fff; }
    .gs-logo span { color:#bbb; }

    /* Hero */
    .gs-hero {
        background:linear-gradient(160deg,#0a0a0a,#161616,#0a0a0a);
        padding:90px 24px; text-align:center;
    }
    .gs-hero-badge {
        display:inline-block; background:rgba(200,200,200,0.08);
        border:1px solid rgba(200,200,200,0.2); color:#aaa;
        font-size:0.65rem; letter-spacing:3px; text-transform:uppercase;
        padding:5px 16px; border-radius:20px; margin-bottom:22px;
    }
    .gs-hero-title { font-family:'Bebas Neue',sans-serif; font-size:5.5rem; letter-spacing:8px; color:#fff; line-height:1; margin-bottom:16px; }
    .gs-hero-title span { color:#bbb; }
    .gs-hero-sub { font-size:1rem; color:#777; max-width:460px; margin:0 auto 36px; line-height:1.7; font-weight:300; }
    .gs-hero-btns { display:flex; gap:14px; justify-content:center; flex-wrap:wrap; margin-bottom:44px; }
    .gs-btn-w  { background:#fff; color:#000; padding:13px 32px; font-size:0.75rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; border-radius:2px; text-decoration:none; display:inline-block; }
    .gs-btn-o  { background:transparent; color:#fff; border:1px solid #444; padding:13px 32px; font-size:0.75rem; font-weight:600; letter-spacing:2px; text-transform:uppercase; border-radius:2px; text-decoration:none; display:inline-block; }
    .gs-contacts { display:flex; gap:14px; justify-content:center; flex-wrap:wrap; }
    .gs-cwpp { background:linear-gradient(135deg,#25D366,#128C7E); color:#fff; padding:11px 22px; border-radius:50px; text-decoration:none; font-size:0.75rem; font-weight:600; letter-spacing:1px; }
    .gs-cig  { background:linear-gradient(135deg,#f09433,#dc2743,#bc1888); color:#fff; padding:11px 22px; border-radius:50px; text-decoration:none; font-size:0.75rem; font-weight:600; letter-spacing:1px; }

    /* Benefits */
    .gs-benefits { background:#111; padding:60px 40px; border-top:1px solid #1e1e1e; border-bottom:1px solid #1e1e1e; }
    .gs-sec-label { text-align:center; font-size:0.65rem; letter-spacing:4px; text-transform:uppercase; color:#555; margin-bottom:8px; }
    .gs-sec-title { font-family:'Bebas Neue',sans-serif; text-align:center; font-size:2.4rem; letter-spacing:4px; color:#fff; margin-bottom:40px; }
    .gs-ben-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:18px; max-width:860px; margin:0 auto; }
    .gs-ben-card { background:#181818; border:1px solid #242424; border-radius:8px; padding:26px 18px; text-align:center; }
    .gs-ben-icon { font-size:1.7rem; margin-bottom:10px; }
    .gs-ben-title { font-weight:700; font-size:0.78rem; letter-spacing:1px; color:#fff; margin-bottom:6px; text-transform:uppercase; }
    .gs-ben-desc { font-size:0.73rem; color:#666; line-height:1.5; }

    /* Catalog header */
    .gs-cat-header { background:#0a0a0a; padding:48px 40px 10px; }

    /* Product info block (abaixo da foto nativa) */
    .gs-pinfo { background:#141414; border:1px solid #1e1e1e; border-radius:0 0 10px 10px; padding:12px 14px 14px; margin-top:-6px; }
    .gs-pbrand { font-size:0.58rem; letter-spacing:2px; text-transform:uppercase; color:#555; margin-bottom:3px; }
    .gs-pname  { font-weight:700; font-size:0.9rem; color:#fff; margin-bottom:4px; line-height:1.2; }
    .gs-pdesc  { font-size:0.72rem; color:#666; line-height:1.4; margin-bottom:8px; }
    .gs-psizes { font-size:0.68rem; color:#888; margin-bottom:8px; letter-spacing:0.5px; }
    .gs-pprice { font-family:'Bebas Neue',sans-serif; font-size:1.3rem; letter-spacing:2px; color:#fff; margin-bottom:10px; }
    .gs-pbadge { display:inline-block; background:#fff; color:#000; font-size:0.58rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; padding:2px 8px; border-radius:2px; margin-bottom:6px; }
    .gs-pbtns  { display:flex; gap:8px; }
    .gs-pwpp { flex:1; background:linear-gradient(135deg,#25D366,#128C7E); color:#fff; padding:9px 4px; border-radius:5px; font-size:0.68rem; font-weight:700; letter-spacing:0.8px; text-decoration:none; text-align:center; text-transform:uppercase; display:block; }
    .gs-pig  { flex:1; background:linear-gradient(135deg,#f09433,#dc2743,#bc1888); color:#fff; padding:9px 4px; border-radius:5px; font-size:0.68rem; font-weight:700; letter-spacing:0.8px; text-decoration:none; text-align:center; text-transform:uppercase; display:block; }

    /* About */
    .gs-about { background:#111; padding:70px 40px; border-top:1px solid #1e1e1e; }
    .gs-about-inner { max-width:640px; margin:0 auto; text-align:center; }
    .gs-about-text { font-size:0.93rem; color:#999; line-height:1.9; font-weight:300; }

    /* Testimonials */
    .gs-testi { background:#0a0a0a; padding:60px 40px; border-top:1px solid #1e1e1e; }
    .gs-tgrid { display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:18px; max-width:900px; margin:0 auto; }
    .gs-tcard { background:#141414; border:1px solid #1e1e1e; border-radius:10px; padding:22px; }
    .gs-stars { color:#f5c518; font-size:0.85rem; margin-bottom:10px; }
    .gs-ttext { font-size:0.8rem; color:#888; line-height:1.6; font-style:italic; margin-bottom:12px; }
    .gs-tauth { font-weight:700; font-size:0.76rem; color:#ccc; }
    .gs-tcity { font-size:0.66rem; color:#555; }

    /* Contact */
    .gs-contact { background:#111; padding:70px 40px; border-top:1px solid #1e1e1e; text-align:center; }
    .gs-cbtns { display:flex; gap:16px; justify-content:center; flex-wrap:wrap; margin-top:30px; }
    .gs-cbtn { display:inline-flex; align-items:center; gap:10px; padding:15px 34px; border-radius:6px; text-decoration:none; font-size:0.82rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; }

    /* Footer */
    .gs-footer { background:#060606; border-top:1px solid #1a1a1a; padding:34px; text-align:center; }
    .gs-flogo  { font-family:'Bebas Neue',sans-serif; font-size:1.6rem; letter-spacing:4px; color:#fff; margin-bottom:12px; }
    .gs-flinks { display:flex; gap:18px; justify-content:center; flex-wrap:wrap; margin-bottom:14px; }
    .gs-flinks a { color:#555; text-decoration:none; font-size:0.68rem; letter-spacing:1.5px; text-transform:uppercase; }
    .gs-flinks a:hover { color:#aaa; }
    .gs-fcopy  { color:#333; font-size:0.66rem; letter-spacing:1px; }

    /* Fix imagem nativa Streamlit */
    [data-testid="stImage"] { border-radius:10px 10px 0 0; overflow:hidden; }
    [data-testid="stImage"] img { border-radius:10px 10px 0 0 !important; object-fit:cover !important; }
    div[data-testid="column"] { padding:4px 6px !important; }
    </style>
    """, unsafe_allow_html=True)


# =============================================
# RENDER CARD — 100% Streamlit nativo, zero HTML inline
# =============================================
def render_card(p):
    wpp = WHATSAPP_BASE + "?text=Olá! Tenho interesse no produto " + p["name"] + " da GS Imports."

    # Container visual do card
    with st.container():
        # Foto
        if os.path.exists(p["image"]):
            st.image(p["image"], use_container_width=True)
        else:
            st.warning("Foto não encontrada: " + p["image"])

        # Badge
        if p["badge"]:
            st.markdown("🆕 **NOVO**")

        # Textos
        st.markdown(
            f"<span style='font-size:0.6rem;color:#555;letter-spacing:2px;text-transform:uppercase;'>"
            f"{p['brand']} · {p['category']}</span>",
            unsafe_allow_html=True
        )
        st.markdown(f"**{p['name']}**")
        st.markdown(
            f"<span style='font-size:0.75rem;color:#666;'>{p['description']}</span>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<span style='font-size:0.72rem;color:#888;'>📏 {p['sizes']}</span>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<span style='font-family:monospace;font-size:1.1rem;font-weight:700;color:#fff;'>{p['price']}</span>",
            unsafe_allow_html=True
        )

        # Botões lado a lado
        b1, b2 = st.columns(2)
        with b1:
            st.link_button("💬 WhatsApp", wpp, use_container_width=True)
        with b2:
            st.link_button("📸 Instagram", INSTAGRAM_URL, use_container_width=True)

        st.divider()


# =============================================
# MAIN
# =============================================
def main():
    st.set_page_config(page_title="GS Imports", page_icon="🖤", layout="wide", initial_sidebar_state="collapsed")
    load_css()

    # NAVBAR
    st.markdown("""<div class="gs-navbar">
        <div class="gs-logo">GS<span> IMPORTS</span></div>
        <span style="color:#555;font-size:0.72rem;letter-spacing:2px;text-transform:uppercase;">São Paulo · SP</span>
    </div>""", unsafe_allow_html=True)

    # HERO
    wpp_hero = WHATSAPP_BASE + "?text=Olá! Vim pelo site e quero saber mais sobre os produtos da GS Imports."
    st.markdown(f"""<div class="gs-hero">
        <div class="gs-hero-badge">✦ Moda Masculina Multimarcas · São Paulo SP</div>
        <div class="gs-hero-title">GS <span>IMPORTS</span></div>
        <p class="gs-hero-sub">Estilo, qualidade e as melhores marcas em um só lugar.</p>
        <div class="gs-hero-btns">
            <a href="#" class="gs-btn-w">Ver Catálogo</a>
            <a href="{wpp_hero}" target="_blank" class="gs-btn-o">Falar no WhatsApp</a>
        </div>
        <div class="gs-contacts">
            <a href="{wpp_hero}" target="_blank" class="gs-cwpp">💬 Entre em contato</a>
            <a href="{INSTAGRAM_URL}" target="_blank" class="gs-cig">📸 Siga no Instagram</a>
        </div>
    </div>""", unsafe_allow_html=True)

    # BENEFITS
    st.markdown("""<div class="gs-benefits">
        <p class="gs-sec-label">Por que nos escolher</p>
        <h2 class="gs-sec-title">NOSSOS DIFERENCIAIS</h2>
        <div class="gs-ben-grid">
            <div class="gs-ben-card"><div class="gs-ben-icon">🎯</div><div class="gs-ben-title">Peças Selecionadas</div><div class="gs-ben-desc">Curadoria rigorosa em cada produto.</div></div>
            <div class="gs-ben-card"><div class="gs-ben-icon">🏷️</div><div class="gs-ben-title">Multimarcas</div><div class="gs-ben-desc">Nike, Fear of God, Tommy, Boss e mais.</div></div>
            <div class="gs-ben-card"><div class="gs-ben-icon">⚡</div><div class="gs-ben-title">Entrega Rápida</div><div class="gs-ben-desc">Envio ágil para todo o Brasil.</div></div>
            <div class="gs-ben-card"><div class="gs-ben-icon">💬</div><div class="gs-ben-title">Atendimento Personalizado</div><div class="gs-ben-desc">Suporte exclusivo via WhatsApp.</div></div>
        </div>
    </div>""", unsafe_allow_html=True)

    # FILTROS
    st.markdown('<div style="background:#0a0a0a;padding:40px 20px 0;">', unsafe_allow_html=True)
    st.markdown('<p class="gs-sec-label" style="margin-bottom:4px;">Encontre o que procura</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="gs-sec-title">CATÁLOGO</h2>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1,1,2])
    with c1: cat   = st.selectbox("Categoria", CATEGORIES)
    with c2: brand = st.selectbox("Marca", BRANDS)
    with c3: srch  = st.text_input("Buscar produto", placeholder="Ex: moletom, Nike, Brasil...")
    st.markdown('</div>', unsafe_allow_html=True)

    # FILTRAGEM
    filtered = PRODUCTS
    if cat   != "Todos":  filtered = [p for p in filtered if p["category"] == cat]
    if brand != "Todas":  filtered = [p for p in filtered if p["brand"] == brand]
    if srch:
        q = srch.lower()
        filtered = [p for p in filtered if q in p["name"].lower() or q in p["brand"].lower()]

    n = len(filtered)
    st.markdown(f'<p style="text-align:center;color:#444;font-size:0.68rem;letter-spacing:2px;text-transform:uppercase;padding:14px 0 6px;">{n} produto{"s" if n!=1 else ""} encontrado{"s" if n!=1 else ""}</p>', unsafe_allow_html=True)

    # GRID DE PRODUTOS — 4 por linha
    st.markdown('<div style="background:#0a0a0a;padding:10px 20px 60px;">', unsafe_allow_html=True)
    cols_per_row = 4
    for i in range(0, len(filtered), cols_per_row):
        row = filtered[i:i+cols_per_row]
        cols = st.columns(cols_per_row)
        for j, p in enumerate(row):
            with cols[j]:
                render_card(p)
    st.markdown('</div>', unsafe_allow_html=True)

    # SOBRE
    st.markdown("""<div class="gs-about">
        <div class="gs-about-inner">
            <p class="gs-sec-label">Quem somos</p>
            <h2 class="gs-sec-title">SOBRE A GS IMPORTS</h2>
            <p class="gs-about-text">
                A <strong style="color:#fff;">GS Imports</strong> é uma loja especializada em moda masculina multimarcas,
                sediada em São Paulo - SP. Trabalhamos com as melhores marcas:
                <strong style="color:#c0c0c0;">Nike, Fear of God, Tommy Hilfiger, Boss</strong> e outras,
                sempre com peças selecionadas e alto padrão de qualidade.<br><br>
                Atendimento personalizado via WhatsApp, entrega rápida e catálogo sempre atualizado.
            </p>
        </div>
    </div>""", unsafe_allow_html=True)

    # DEPOIMENTOS
    st.markdown("""<div class="gs-testi">
        <p class="gs-sec-label">O que dizem nossos clientes</p>
        <h2 class="gs-sec-title">DEPOIMENTOS</h2>
        <div class="gs-tgrid">
            <div class="gs-tcard"><div class="gs-stars">★★★★★</div><p class="gs-ttext">"Produto chegou rapidíssimo e a qualidade é impecável. O moletom Fear of God superou todas as expectativas!"</p><div class="gs-tauth">Rafael M.</div><div class="gs-tcity">São Paulo - SP</div></div>
            <div class="gs-tcard"><div class="gs-stars">★★★★★</div><p class="gs-ttext">"Atendimento excelente pelo WhatsApp. Já fiz 3 pedidos e sempre saio satisfeito."</p><div class="gs-tauth">Lucas S.</div><div class="gs-tcity">São Paulo - SP</div></div>
            <div class="gs-tcard"><div class="gs-stars">★★★★★</div><p class="gs-ttext">"Melhor loja de multimarcas de SP. Peças originais, preço justo e entrega no prazo!"</p><div class="gs-tauth">Pedro A.</div><div class="gs-tcity">São Paulo - SP</div></div>
        </div>
    </div>""", unsafe_allow_html=True)

    # CONTATO
    wpp_contact = WHATSAPP_BASE + "?text=Olá! Vim pelo site da GS Imports e gostaria de mais informações."
    st.markdown(f"""<div class="gs-contact">
        <p class="gs-sec-label">Fale conosco</p>
        <h2 class="gs-sec-title">CONTATO</h2>
        <p style="color:#666;font-size:0.83rem;max-width:400px;margin:0 auto;line-height:1.7;">
            Atendimento de segunda a sábado, das 9h às 21h.
        </p>
        <div class="gs-cbtns">
            <a href="{wpp_contact}" target="_blank" class="gs-cbtn" style="background:linear-gradient(135deg,#25D366,#128C7E);color:#fff;">💬 Chamar no WhatsApp</a>
            <a href="{INSTAGRAM_URL}" target="_blank" class="gs-cbtn" style="background:linear-gradient(135deg,#f09433,#dc2743,#bc1888);color:#fff;">📸 Ver no Instagram</a>
        </div>
    </div>""", unsafe_allow_html=True)

    # FOOTER
    st.markdown(f"""<div class="gs-footer">
        <div class="gs-flogo">GS IMPORTS</div>
        <div class="gs-flinks">
            <a href="{INSTAGRAM_URL}" target="_blank">Instagram</a>
            <a href="{WHATSAPP_BASE}" target="_blank">WhatsApp</a>
        </div>
        <p class="gs-fcopy">© 2025 GS Imports · São Paulo - SP · Todos os direitos reservados</p>
    </div>""", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
