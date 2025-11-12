// Common utility functions
function showLoading(loadingEl) {
    if (loadingEl) {
        loadingEl.style.display = 'block';
    }
}

function hideLoading(loadingEl) {
    if (loadingEl) {
        loadingEl.style.display = 'none';
    }
}

function showResults(resultsEl) {
    if (resultsEl) {
        resultsEl.style.display = 'block';
        resultsEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

function hideResults(resultsEl) {
    if (resultsEl) {
        resultsEl.style.display = 'none';
    }
}

function showError(message) {
    alert('Error: ' + message);
}
