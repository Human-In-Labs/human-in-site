(() => {
  "use strict";

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // 1. Floating header glass effect on scroll
  const headerPill = document.querySelector("[data-header]");
  if (headerPill) {
    const scrolledClasses = (headerPill.dataset.scrolledClasses || "").split(/\s+/).filter(Boolean);
    const topClasses = (headerPill.dataset.topClasses || "").split(/\s+/).filter(Boolean);

    const syncHeader = () => {
      const scrolled = window.scrollY > 24;
      for (const cls of scrolledClasses) headerPill.classList.toggle(cls, scrolled);
      for (const cls of topClasses) headerPill.classList.toggle(cls, !scrolled);
    };

    syncHeader();
    window.addEventListener("scroll", syncHeader, { passive: true });
  }

  // 2. Mobile menu drawer toggle
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const mobileMenu = document.querySelector("[data-mobile-menu]");
  const iconOpen = document.querySelector("[data-menu-icon-open]");
  const iconClose = document.querySelector("[data-menu-icon-close]");

  const setMenuOpen = (open) => {
    if (!menuToggle || !mobileMenu) return;
    mobileMenu.hidden = !open;
    menuToggle.setAttribute("aria-expanded", String(open));
    menuToggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    if (iconOpen) iconOpen.hidden = open;
    if (iconClose) iconClose.hidden = !open;
  };

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener("click", () => {
      setMenuOpen(mobileMenu.hidden);
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !mobileMenu.hidden) {
        setMenuOpen(false);
        menuToggle.focus();
      }
    });
  }

  // 3. Centered smooth anchor scroll + closing mobile menu
  const scrollToSection = (event, href) => {
    const id = href.slice(1);
    const target = document.getElementById(id);
    if (!target) return;

    event.preventDefault();
    const styles = window.getComputedStyle(target);
    const padTop = parseFloat(styles.paddingTop) || 0;
    const padBottom = parseFloat(styles.paddingBottom) || 0;
    const rect = target.getBoundingClientRect();
    const contentTop = rect.top + window.scrollY + padTop;
    const contentHeight = rect.height - padTop - padBottom;
    const viewportAvailable = window.innerHeight - 88;

    const top =
      id === "inicio"
        ? 0
        : contentHeight < viewportAvailable
          ? contentTop - 88 - (viewportAvailable - contentHeight) / 2
          : contentTop - 88 - 24;

    window.scrollTo({
      top: Math.max(0, top),
      behavior: reducedMotion ? "auto" : "smooth",
    });
    history.replaceState(null, "", href);
  };

  document.addEventListener("click", (event) => {
    const closeTrigger = event.target.closest("[data-menu-close]");
    if (closeTrigger && mobileMenu && !mobileMenu.hidden) {
      setMenuOpen(false);
    }

    const anchor = event.target.closest("a[href^='#']");
    if (!anchor) return;
    const href = anchor.getAttribute("href");
    if (!href || href === "#") return;

    scrollToSection(event, href);
    if (mobileMenu && !mobileMenu.hidden) {
      setMenuOpen(false);
    }
  });

  // 4. Scroll reveal animations
  const revealItems = document.querySelectorAll(".reveal");
  if (revealItems.length > 0) {
    if (reducedMotion || !("IntersectionObserver" in window)) {
      revealItems.forEach((el) => el.setAttribute("data-visible", "true"));
    } else {
      const observer = new IntersectionObserver(
        (entries) => {
          for (const entry of entries) {
            if (entry.isIntersecting) {
              entry.target.setAttribute("data-visible", "true");
              observer.unobserve(entry.target);
            }
          }
        },
        { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
      );
      revealItems.forEach((el) => observer.observe(el));
    }
  }

  // 5. Contact form mailto handler
  const contactForm = document.querySelector("[data-contact-form]");
  if (contactForm) {
    contactForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const formData = new FormData(contactForm);
      const nome = String(formData.get("nome") ?? "").trim();
      const email = String(formData.get("email") ?? "").trim();
      const mensagem = String(formData.get("mensagem") ?? "").trim();

      const subject = encodeURIComponent(`Contato pelo site — ${nome || "Visitante"}`);
      const body = encodeURIComponent(`Nome: ${nome}\nE-mail: ${email}\n\n${mensagem}`);
      window.location.href = `mailto:contato@humanin.com.br?subject=${subject}&body=${body}`;
    });
  }
})();
