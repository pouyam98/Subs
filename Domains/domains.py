import json

def extract_domains(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    domains = [item['domain'] for item in data['data']]
    
    with open(output_file, 'w') as f:
        for domain in domains:
            f.write(f"{domain}\n")

if __name__ == "__main__":
    extract_domains('input.json', 'output.txt')

