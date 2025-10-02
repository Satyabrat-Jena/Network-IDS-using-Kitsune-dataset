// Main JavaScript for Malignant Packet Logger

// Web3 initialization
let web3;
let contract;
let account;

// Initialize Web3 connection
async function initWeb3() {
    // Check if Web3 is injected by MetaMask
    if (window.ethereum) {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            web3 = new Web3(window.ethereum);
            console.log("Using Web3 injected by MetaMask");
            return true;
        } catch (error) {
            console.error("User denied account access");
        }
    } 
    // Fallback to local provider (for demo purposes)
    else {
        web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));
        console.log("Using local Web3 provider");
        return true;
    }
    return false;
}

// Load contract
async function loadContract(contractAddress, contractABI) {
    if (!web3) {
        console.error("Web3 not initialized");
        return false;
    }
    
    try {
        // Create contract instance
        contract = new web3.eth.Contract(contractABI, contractAddress);
        console.log("Contract loaded successfully");
        
        // Get accounts
        const accounts = await web3.eth.getAccounts();
        account = accounts[0];
        console.log("Using account:", account);
        
        return true;
    } catch (error) {
        console.error("Error loading contract:", error);
        return false;
    }
}

// Format timestamp
function formatTimestamp(timestamp) {
    const date = new Date(timestamp * 1000);
    return date.toLocaleString();
}

// Copy to clipboard function
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        console.log('Copying to clipboard was successful!');
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}

// Show notification
function showNotification(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    
    const toastContainer = document.getElementById('toastContainer');
    if (!toastContainer) {
        const container = document.createElement('div');
        container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        container.id = 'toastContainer';
        document.body.appendChild(container);
    }
    
    document.getElementById('toastContainer').appendChild(toast);
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    // Remove toast after it's hidden
    toast.addEventListener('hidden.bs.toast', function () {
        toast.remove();
    });
}

// Document ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Add toast container if it doesn't exist
    if (!document.getElementById('toastContainer')) {
        const container = document.createElement('div');
        container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        container.id = 'toastContainer';
        document.body.appendChild(container);
    }
});
