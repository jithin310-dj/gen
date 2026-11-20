"""Prompt enhancement helpers for technical illustration generation."""

STYLE_PROMPTS = {
    "Professional 3D": (
        "professional 3D technical illustration, clean composition, "
        "soft realistic lighting, clear visual hierarchy"
    ),
    "Flat Vector": (
        "flat vector illustration, minimal design, clean geometric shapes, "
        "simple coordinated colors, crisp edges"
    ),
    "Blueprint": (
        "engineering blueprint aesthetic, precise technical drawing, "
        "fine white lines on a deep blue background"
    ),
    "Isometric": (
        "isometric technical illustration, consistent perspective, "
        "well-organized components, clean professional design"
    )
}


def enhance_prompt(user_prompt: str, style: str) -> str:
    style_text = STYLE_PROMPTS.get(style, STYLE_PROMPTS["Professional 3D"])
    return (
        f"{user_prompt}. {style_text}. "
        "High quality, balanced composition, clear spacing, "
        "suitable for software and technical documentation."
    )


def get_negative_prompt() -> str:
    return (
        "blurry, low quality, distorted objects, messy composition, "
        "poor lighting, watermark, signature, low resolution, "
        "unwanted text, misspelled words"
    )
