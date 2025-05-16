import typer
import pandas as pd
import yaml
import re

app = typer.Typer()

def load_config(config_path):
    with open(config_path) as f:
        return yaml.safe_load(f)

def validate(config):
    df = pd.read_csv(config["dataset"])
    print(f"🔍 Validating dataset: {config['dataset']}")

    for rule in config["rules"]:
        col = rule["column"]
        check = rule["check"]

        if col not in df.columns:
            print(f"❌ Column '{col}' not found.")
            continue

        if check == "not_null":
            if df[col].isnull().any():
                print(f"❌ Nulls found in '{col}'")
            else:
                print(f"✅ '{col}' passed not_null check")

        elif check == "unique":
            if df[col].duplicated().any():
                print(f"❌ Duplicates found in '{col}'")
            else:
                print(f"✅ '{col}' is unique")

        elif check == "range":
            min_val = rule["min"]
            max_val = rule["max"]
            if df[col].min() < min_val or df[col].max() > max_val:
                print(f"❌ Values in '{col}' out of range ({min_val}-{max_val})")
            else:
                print(f"✅ '{col}' is within range")

        elif check == "regex":
            pattern = re.compile(rule["pattern"])
            if not df[col].astype(str).str.match(pattern).all():
                print(f"❌ Some values in '{col}' fail regex check")
            else:
                print(f"✅ '{col}' passed regex check")

        else:
            print(f"⚠️ Unknown check: {check}")

@app.command()
@app.command()
def run(config: str = typer.Argument(..., help="Path to the YAML config file")):
    "Run data quality checks from a YAML config file."
    config_data = load_config(config)
    validate(config_data)

if __name__ == "__main__":
    app()