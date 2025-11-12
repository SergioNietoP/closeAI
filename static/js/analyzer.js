document.addEventListener('DOMContentLoaded', function() {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const textInput = document.getElementById('text');
    const analysisType = document.getElementById('analysisType');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const resultsContent = document.getElementById('resultsContent');

    analyzeBtn.addEventListener('click', async function() {
        const text = textInput.value.trim();
        const type = analysisType.value;

        if (!text) {
            showError('Please enter text to analyze.');
            return;
        }

        showLoading(loading);
        hideResults(results);
        analyzeBtn.disabled = true;

        try {
            const response = await fetch('/api/analyze-text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text, type })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Failed to analyze text');
            }

            displayAnalysis(data.analysis);
            showResults(results);
        } catch (error) {
            showError(error.message);
        } finally {
            hideLoading(loading);
            analyzeBtn.disabled = false;
        }
    });

    function displayAnalysis(analysis) {
        const html = `<div class="explanation">${analysis.replace(/\n/g, '<br>')}</div>`;
        resultsContent.innerHTML = html;
    }
});
