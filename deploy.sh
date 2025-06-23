#!/bin/bash

# Chainlink MCP Server Deployment Script
# This script helps you deploy the MCP server to GitHub Pages

set -e

echo "🔗 Chainlink MCP Server Deployment"
echo "=================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ This is not a git repository. Initializing..."
    git init
    git branch -M main
fi

# Check if we have a remote
if ! git remote get-url origin >/dev/null 2>&1; then
    echo ""
    echo "🔗 Setting up Git remote"
    echo "Please enter your GitHub repository URL (e.g., https://github.com/username/chainlink-tooling.git):"
    read -r repo_url
    git remote add origin "$repo_url"
    
    # Extract username and repo name for updating mcp-server.json
    if [[ $repo_url =~ github\.com[:/]([^/]+)/([^/\.]+) ]]; then
        username="${BASH_REMATCH[1]}"
        repo_name="${BASH_REMATCH[2]}"
        
        echo "📝 Updating mcp-server.json with your repository info..."
        sed -i.bak "s/yourusername/$username/g" mcp-server.json
        sed -i.bak "s/chainlink-tooling/$repo_name/g" mcp-server.json
        rm mcp-server.json.bak 2>/dev/null || true
        
        echo "📝 Updating README.md with your repository info..."
        sed -i.bak "s/YOUR_USERNAME/$username/g" README.md
        sed -i.bak "s/chainlink-tooling/$repo_name/g" README.md
        rm README.md.bak 2>/dev/null || true
    fi
fi

# Validate JSON files
echo ""
echo "✅ Validating JSON files..."
for file in mcp-server.json tools/*.json; do
    if [ -f "$file" ]; then
        echo "  Checking $file..."
        python -m json.tool < "$file" > /dev/null
        echo "  ✓ $file is valid"
    fi
done

# Stage and commit files
echo ""
echo "📦 Staging files for deployment..."
git add .

if git diff --staged --quiet; then
    echo "ℹ️  No changes to commit"
else
    echo "💾 Committing changes..."
    git commit -m "Deploy Chainlink MCP Server to GitHub Pages"
fi

# Push to GitHub
echo ""
echo "🚀 Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📋 Next steps:"
echo "1. Go to your GitHub repository settings"
echo "2. Navigate to Pages section"
echo "3. Select 'Deploy from a branch'"
echo "4. Choose 'main' branch and '/ (root)' folder"
echo "5. Save settings"
echo ""
echo "🌐 Your MCP server will be available at:"
if [[ $repo_url =~ github\.com[:/]([^/]+)/([^/\.]+) ]]; then
    echo "   https://${BASH_REMATCH[1]}.github.io/${BASH_REMATCH[2]}/"
    echo ""
    echo "🔗 MCP endpoint URL for Cursor IDE:"
    echo "   https://${BASH_REMATCH[1]}.github.io/${BASH_REMATCH[2]}/mcp-server.json"
else
    echo "   https://USERNAME.github.io/REPOSITORY_NAME/"
fi

echo ""
echo "⏱️  Note: GitHub Pages deployment may take a few minutes to become available." 