#!/usr/bin/env python3
"""
Chainlink MCP Server Validation Script
Validates the structure and content of the MCP server files
"""

import json
import os
import sys
from pathlib import Path

def validate_json_file(filepath):
    """Validate that a file contains valid JSON"""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def validate_mcp_server_manifest():
    """Validate the main MCP server manifest file"""
    print("🔍 Validating MCP server manifest...")
    
    if not os.path.exists('mcp-server.json'):
        print("❌ mcp-server.json not found")
        return False
    
    valid, error = validate_json_file('mcp-server.json')
    if not valid:
        print(f"❌ mcp-server.json is not valid JSON: {error}")
        return False
    
    with open('mcp-server.json', 'r') as f:
        data = json.load(f)
    
    # Check required fields
    required_fields = ['name', 'version', 'mcp', 'tools']
    for field in required_fields:
        if field not in data:
            print(f"❌ Missing required field: {field}")
            return False
    
    # Check MCP version
    if 'mcp' in data and 'version' in data['mcp']:
        mcp_version = data['mcp']['version']
        if mcp_version != '1.0.0':
            print(f"⚠️  MCP version {mcp_version} may not be compatible")
    
    # Validate tool references
    if 'tools' in data:
        for tool_ref in data['tools']:
            if 'source' not in tool_ref:
                print(f"❌ Tool reference missing 'source' field: {tool_ref}")
                return False
            
            tool_path = tool_ref['source'].lstrip('./')
            if not os.path.exists(tool_path):
                print(f"❌ Tool file not found: {tool_path}")
                return False
    
    print("✅ MCP server manifest is valid")
    return True

def validate_tool_files():
    """Validate all tool definition files"""
    print("\n🔧 Validating tool files...")
    
    tools_dir = Path('tools')
    if not tools_dir.exists():
        print("❌ tools/ directory not found")
        return False
    
    tool_files = list(tools_dir.glob('*.json'))
    if not tool_files:
        print("❌ No tool files found in tools/ directory")
        return False
    
    total_tools = 0
    for tool_file in tool_files:
        print(f"  Checking {tool_file}...")
        
        valid, error = validate_json_file(tool_file)
        if not valid:
            print(f"❌ {tool_file} is not valid JSON: {error}")
            return False
        
        with open(tool_file, 'r') as f:
            data = json.load(f)
        
        # Check if it's a tools array or object with tools property
        if isinstance(data, list):
            tools = data
        elif isinstance(data, dict) and 'tools' in data:
            tools = data['tools']
        else:
            print(f"❌ {tool_file} does not contain a valid tools structure")
            return False
        
        file_tool_count = len(tools)
        total_tools += file_tool_count
        
        # Validate each tool
        for i, tool in enumerate(tools):
            if not isinstance(tool, dict):
                print(f"❌ Tool {i} in {tool_file} is not an object")
                return False
            
            # Check for required fields (handle both inputSchema and input_schema)
            required_tool_fields = ['name', 'description']
            for field in required_tool_fields:
                if field not in tool:
                    print(f"❌ Tool {i} in {tool_file} missing required field: {field}")
                    return False
            
            # Check for schema field (either inputSchema or input_schema)
            if 'inputSchema' not in tool and 'input_schema' not in tool:
                print(f"❌ Tool {i} in {tool_file} missing input schema field (inputSchema or input_schema)")
                return False
        
        print(f"  ✅ {tool_file} contains {file_tool_count} valid tools")
    
    print(f"\n✅ All tool files are valid ({total_tools} total tools)")
    return True

def validate_file_structure():
    """Validate the overall file structure"""
    print("\n📁 Validating file structure...")
    
    required_files = [
        'index.html',
        'mcp-server.json', 
        'README.md',
        'tools/index.html'
    ]
    
    required_dirs = [
        'tools',
        'docs',
        '.github/workflows'
    ]
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"❌ Required file missing: {file_path}")
            return False
        print(f"  ✅ {file_path}")
    
    for dir_path in required_dirs:
        if not os.path.isdir(dir_path):
            print(f"❌ Required directory missing: {dir_path}")
            return False
        print(f"  ✅ {dir_path}/")
    
    print("✅ File structure is valid")
    return True

def validate_html_files():
    """Basic validation of HTML files"""
    print("\n🌐 Validating HTML files...")
    
    html_files = ['index.html', 'tools/index.html']
    
    for html_file in html_files:
        if os.path.exists(html_file):
            with open(html_file, 'r') as f:
                content = f.read()
            
            # Basic HTML validation
            if not content.strip().startswith('<!DOCTYPE html>'):
                print(f"❌ {html_file} missing DOCTYPE declaration")
                return False
            
            if 'mcp-server' not in content and html_file == 'index.html':
                print(f"❌ {html_file} missing MCP server references")
                return False
            
            print(f"  ✅ {html_file}")
    
    print("✅ HTML files are valid")
    return True

def main():
    """Main validation function"""
    print("🔗 Chainlink MCP Server Validation")
    print("===================================")
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    all_valid = True
    
    # Run all validations
    validations = [
        validate_file_structure,
        validate_mcp_server_manifest,
        validate_tool_files,
        validate_html_files
    ]
    
    for validation in validations:
        if not validation():
            all_valid = False
    
    print("\n" + "="*50)
    if all_valid:
        print("🎉 All validations passed! Your MCP server is ready for deployment.")
        print("\n📋 Next steps:")
        print("1. Run './deploy.sh' to deploy to GitHub Pages")
        print("2. Or manually push to your GitHub repository")
        print("3. Enable GitHub Pages in repository settings")
        return 0
    else:
        print("❌ Some validations failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 