#!/usr/bin/env python3
import os
import json
import argparse
import yaml
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

LANGUAGES = {
    "en": "English",
    "fr": "French",
    "eu": "Euskera",
    "es": "Spanish",
    "ca": "Catalan",
    "pt": "Portuguese",
}

def load_config(config_path="config.yaml"):
    """Load API key and settings from config file"""
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    return {}

def translate_text(api_key, text, source_lang, target_lang):
    """Translates a text segment using OpenAI API"""
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a translator from {source_lang} to {target_lang}."},
            {"role": "user", "content": text}
        ],
        max_tokens=2048,  # Ensure safe token usage
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()

def split_large_json(json_obj, chunk_size=1000):
    """Splits large JSON structures into smaller chunks"""
    if isinstance(json_obj, dict):
        return {k: v[:chunk_size] if isinstance(v, list) else v for k, v in json_obj.items()}
    elif isinstance(json_obj, list):
        return json_obj[:chunk_size]
    return json_obj  # Return as is if not a list or dict

def translate_json(api_key, json_data, source_lang, target_lang):
    """Recursively translates JSON while preserving structure"""
    if isinstance(json_data, dict):
        return {key: translate_json(api_key, value, source_lang, target_lang) for key, value in json_data.items()}
    elif isinstance(json_data, list):
        return [translate_json(api_key, item, source_lang, target_lang) for item in json_data]
    elif isinstance(json_data, str):
        return translate_text(api_key, json_data, source_lang, target_lang)
    return json_data  # Return unchanged for numbers, booleans, etc.

def translate_json_file(api_key, input_path, output_path, source_lang, target_lang, chunk_size=1000):
    """Handles large JSON translation in chunks"""
    with open(input_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    # Split large JSON if needed
    json_data = split_large_json(json_data, chunk_size)

    # Translate JSON
    translated_json = translate_json(api_key, json_data, source_lang, target_lang)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(translated_json, file, ensure_ascii=False, indent=4)

    print(f"✅ JSON Translation completed: {input_path} → {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate a JSON file using OpenAI API")
    parser.add_argument("input_file", help="Path to the input JSON file")
    parser.add_argument("output_file", help="Path to save the translated JSON file")
    parser.add_argument("--source_language", choices=LANGUAGES.keys(), help="Source language (auto-detect if omitted)")
    parser.add_argument("--target_language", required=True, choices=LANGUAGES.keys(), help="Target language")
    parser.add_argument("--config", default="config.yaml", help="Path to configuration file")
    parser.add_argument("--chunk_size", type=int, default=1000, help="Chunk size for processing large JSON files")

    args = parser.parse_args()

    config = load_config(args.config)
    api_key = os.getenv("OPENAI_API_KEY", config.get("OPENAI_API_KEY"))

    if not api_key:
        print("❌ Error: Missing OpenAI API key. Set it in .env or config.yaml")
        exit(1)

    translate_json_file(api_key, args.input_file, args.output_file, args.source_language, args.target_language, args.chunk_size)

