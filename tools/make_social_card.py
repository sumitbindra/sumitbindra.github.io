#!/usr/bin/env python3
"""
Generate social share card image (1200x630) for sumitbindra.com
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Image dimensions for social share cards
WIDTH = 1200
HEIGHT = 630

# Dark navy background
BACKGROUND_COLOR = "#1a2332"

# White text for high contrast
TEXT_COLOR = "#ffffff"

# Accent color for footer
ACCENT_COLOR = "#60a5fa"

# Margins and layout
MARGIN_X = 80
MARGIN_Y = 80


def create_social_card(output_path):
    """Create the social share card image"""
    
    # Create image with dark background
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Try to use DejaVu Sans, fall back to default if not available
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        font_footer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    except OSError:
        # Fallback to default font
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_footer = ImageFont.load_default()
    
    # Starting Y position
    y_position = MARGIN_Y
    
    # Draw main name (large)
    text_name = "Sumit Bindra"
    draw.text((MARGIN_X, y_position), text_name, font=font_large, fill=TEXT_COLOR)
    y_position += 100
    
    # Draw title (medium)
    text_title = "Applied AI Engineer"
    draw.text((MARGIN_X, y_position), text_title, font=font_medium, fill=TEXT_COLOR)
    y_position += 70
    
    # Draw specialties (smaller)
    text_specialty1 = "Multi-agent LLM systems · Voice AI · MCP servers"
    draw.text((MARGIN_X, y_position), text_specialty1, font=font_small, fill=TEXT_COLOR)
    y_position += 50
    
    # Draw experience (smaller)
    text_experience = "15 years of transportation data modeling"
    draw.text((MARGIN_X, y_position), text_experience, font=font_small, fill=TEXT_COLOR)
    
    # Draw footer/domain at bottom
    footer_text = "sumitbindra.com"
    footer_y = HEIGHT - MARGIN_Y - 30
    draw.text((MARGIN_X, footer_y), footer_text, font=font_footer, fill=ACCENT_COLOR)
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save with optimization
    img.save(output_path, 'PNG', optimize=True)
    
    # Print file size
    file_size = os.path.getsize(output_path)
    print(f"Social card created: {output_path}")
    print(f"Size: {file_size:,} bytes ({file_size / 1024:.1f} KB)")


if __name__ == "__main__":
    # Output path relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    output_path = os.path.join(repo_root, "assets", "images", "social-card.png")
    
    create_social_card(output_path)
