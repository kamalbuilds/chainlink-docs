# 🔗 Chainlink MCP Server

A production-ready Model Context Protocol (MCP) server providing comprehensive tools for all major Chainlink services. Designed for AI agents and automated systems building cross-chain applications.

## 🌟 Overview

This MCP server provides 57+ production-ready tools across 5 core Chainlink services:

- **CCIP** (10 tools) - Cross-chain interoperability protocol
- **Data Streams** (10 tools) - High-frequency market data feeds  
- **Functions** (12 tools) - Serverless JavaScript execution
- **VRF** (12 tools) - Verifiable random function
- **Automation** (13 tools) - Decentralized job scheduling

## 🚀 Quick Start

### Using with Cursor IDE

1. **Copy the MCP server URL:**
   ```
   https://your-username.github.io/chainlink-tooling/mcp-server.json
   ```

2. **Add to Cursor MCP configuration:**
   ```json
   {
     "mcpServers": {
       "chainlink": {
         "command": "mcp-server-http",
         "args": ["https://your-username.github.io/chainlink-tooling/mcp-server.json"]
       }
     }
   }
   ```

3. **Start using Chainlink tools in your AI conversations!**

### Using with Other MCP Clients

The server follows the standard MCP specification and can be used with any compatible client:

```bash
# Install MCP client
npm install @modelcontextprotocol/client

# Connect to server
const client = new MCPClient("https://your-username.github.io/chainlink-tooling/mcp-server.json");
```

## 🛠️ Available Services

### CCIP (Cross-Chain Interoperability Protocol)
- Send cross-chain messages and tokens
- Estimate fees and track transactions
- Support for 9+ blockchain networks
- Automatic retry and error handling

### Data Streams (High-Frequency Oracle Data)
- Real-time market data via REST API
- WebSocket subscriptions for live updates
- Onchain report verification
- Bulk data retrieval and caching

### Functions (Serverless Compute)
- Execute custom JavaScript code
- Manage secrets and encryption
- Cost estimation and optimization
- Local simulation and testing

### VRF (Verifiable Random Function)
- Generate cryptographically secure randomness
- Proof verification and validation
- Subscription and consumer management
- Batch requests for efficiency

### Automation (Decentralized Job Scheduling)
- Time-based and conditional triggers
- Log-based automation
- Upkeep management and funding
- Performance monitoring

## 🌐 Supported Networks

- Ethereum Mainnet
- Polygon 
- Arbitrum One
- Avalanche C-Chain
- Base
- BNB Smart Chain
- Fantom Opera
- Optimism
- Solana

## 📋 Prerequisites

To use these tools in production, you'll need:

1. **API Keys** (for Data Streams and Functions)
2. **Private Keys** (for transaction signing)
3. **RPC Endpoints** (for blockchain connections)
4. **Native Tokens** (for gas fees)

## 🔧 Environment Variables

```bash
# Chainlink Configuration
CHAINLINK_API_KEY=your_api_key
CHAINLINK_API_SECRET=your_api_secret

# Blockchain Networks
ETHEREUM_RPC_URL=https://eth-mainnet.alchemyapi.io/v2/your-key
POLYGON_RPC_URL=https://polygon-rpc.com
ARBITRUM_RPC_URL=https://arb1.arbitrum.io/rpc
# ... other networks

# Private Keys (Use secure key management)
ETHEREUM_PRIVATE_KEY=0x...
POLYGON_PRIVATE_KEY=0x...
# ... other networks

# AI Services (for Functions)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

## 📁 Project Structure

```
chainlink-tooling/
├── index.html              # Main landing page
├── mcp-server.json         # MCP server manifest
├── tools/                  # Tool definitions
│   ├── index.html         # Tools browser
│   ├── ccip.json          # CCIP tools
│   ├── data-streams.json  # Data Streams tools
│   ├── functions.json     # Functions tools
│   ├── vrf.json           # VRF tools
│   └── automation.json    # Automation tools
├── docs/                  # Documentation files
│   ├── ccip.txt          # CCIP documentation
│   ├── data-streams.llm-full.txt
│   ├── functions.txt
│   ├── vrf.llm.txt
│   └── chainlink-automation.txt
└── README.md              # This file
```

## 🚢 Deployment to GitHub Pages

1. **Fork or clone this repository**

2. **Update the repository URL in `mcp-server.json`:**
   ```json
   {
     "repository": {
       "url": "https://github.com/YOUR_USERNAME/chainlink-tooling"
     }
   }
   ```

3. **Push to your GitHub repository:**
   ```bash
   git add .
   git commit -m "Deploy Chainlink MCP Server"
   git push origin main
   ```

4. **Enable GitHub Pages:**
   - Go to repository Settings
   - Navigate to Pages section
   - Select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Save settings

5. **Access your MCP server:**
   ```
   https://YOUR_USERNAME.github.io/chainlink-tooling/
   ```

## 🔍 Tool Examples

### Send Cross-Chain Message (CCIP)
```json
{
  "tool": "chainlink_ccip_send_message",
  "parameters": {
    "destinationNetwork": "polygon",
    "sourceNetwork": "ethereum", 
    "recipientAddress": "0x...",
    "message": "Hello cross-chain!",
    "gasLimit": 200000
  }
}
```

### Get Real-Time Price Data (Data Streams)
```json
{
  "tool": "chainlink_data_streams_get_latest_report",
  "parameters": {
    "feedId": "0x00024...ETH/USD",
    "network": "ethereum"
  }
}
```

### Execute Custom Code (Functions)
```json
{
  "tool": "chainlink_functions_send_request",
  "parameters": {
    "source": "return Functions.encodeString('Hello World');",
    "subscriptionId": 123,
    "gasLimit": 300000,
    "network": "polygon"
  }
}
```

## 🔒 Security Considerations

- **Private Keys**: Never commit private keys to version control
- **API Keys**: Use environment variables for sensitive data
- **Rate Limiting**: Implement proper rate limiting for API calls
- **Gas Management**: Monitor gas costs and set appropriate limits
- **Error Handling**: All tools include comprehensive error handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add or improve tools following the existing pattern
4. Test thoroughly with real blockchain interactions
5. Submit a pull request

## 📚 Documentation

- [Chainlink Documentation](https://docs.chain.link)
- [MCP Specification](https://spec.modelcontextprotocol.io)
- [Tool Development Guide](./docs/)

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

- [Chainlink Discord](https://discord.gg/chainlink)
- [GitHub Issues](https://github.com/YOUR_USERNAME/chainlink-tooling/issues)
- [Chainlink Developer Hub](https://dev.chain.link)

---

**Built for the Cross-Chain AI Prediction Market Arbitrage Network**  
*Production-ready • Multi-blockchain • Agent-optimized* 