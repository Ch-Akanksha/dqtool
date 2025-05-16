# 🧪 dqtool — Data Quality as Code

A lightweight CLI tool to validate your data using declarative YAML configs.

## 🔧 Features
- Define data quality rules in YAML
- Run via CLI
- Supports: nulls, ranges, uniqueness, regex
- Easy to integrate into CI/CD

## 🚀 Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run validation
python dqcli.py run examples/users_rules.yaml
