async function connectWallet() {
  //e.preventDefault();
  if (typeof window.ethereum !== 'undefined') {
    try {
      await window.ethereum.request({
        method: 'wallet_addEthereumChain',
        params: [{
          chainId: '0xAE3F3',
          chainName: 'Sei Network',
          nativeCurrency: {
            name: 'Sei token',
            symbol: 'SEI',
            decimals: 18
          },
          rpcUrls: ['https://evm-rpc-arctic-1.sei-apis.com'],
          blockExplorerUrls: ['https://explorer.galadriel.com']
        }]
      });
    } catch (addError) {
      console.error('Error adding Sei network to MetaMask', addError);
    }
  } else {
    console.log('Ethereum provider not found. Install MetaMask.');
  }
};

// This works without onContentLoaded because Mintlify renders the DOM server-side - TP 07.03.24
const pElement = document.getElementById("connect-wallet-p");
const aElement = document.createElement("a");
aElement.textContent = "Connect Wallet";
aElement.href = "#";
aElement.onclick = function(event) {
    event.preventDefault();
    connectWallet();
};
let res = pElement.appendChild(aElement);
console.log("res", res);
