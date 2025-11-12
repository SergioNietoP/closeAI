document.addEventListener('DOMContentLoaded', function() {
    const evaluateBtn = document.getElementById('evaluateBtn');
    const questionInput = document.getElementById('question');
    const answerInput = document.getElementById('answer');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const resultsContent = document.getElementById('resultsContent');

    evaluateBtn.addEventListener('click', async function() {
        const question = questionInput.value.trim();
        const answer = answerInput.value.trim();

        if (!question || !answer) {
            showError('Please enter both a question and an answer.');
            return;
        }

        showLoading(loading);
        hideResults(results);
        evaluateBtn.disabled = true;

        try {
            const response = await fetch('/api/evaluate-answer', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question, answer })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Failed to evaluate answer');
            }

            displayEvaluation(data.evaluation);
            showResults(results);
        } catch (error) {
            showError(error.message);
        } finally {
            hideLoading(loading);
            evaluateBtn.disabled = false;
        }
    });

    function displayEvaluation(evaluation) {
        if (evaluation.raw) {
            // Display raw text response
            resultsContent.innerHTML = `<div class="explanation">${evaluation.raw.replace(/\n/g, '<br>')}</div>`;
            return;
        }

        let html = '';

        // Display scores
        const scoreFields = ['Specificity', 'Relevance', 'Problem-Solving', 'Initiative', 'Outcome', 'Self-Reflection', 'Creativity', 'Communication'];
        const scores = scoreFields.filter(field => evaluation[field] !== undefined);

        if (scores.length > 0) {
            html += '<div class="score-grid">';
            scores.forEach(field => {
                html += `
                    <div class="score-item">
                        <div class="label">${field}</div>
                        <div class="value">${evaluation[field]}/10</div>
                    </div>
                `;
            });
            html += '</div>';
        }

        // Display average
        if (evaluation.average !== undefined) {
            html += `
                <div class="score-item" style="margin: 1.5rem auto; max-width: 300px;">
                    <div class="label">Average Score</div>
                    <div class="value" style="font-size: 2.5rem;">${evaluation.average}/10</div>
                </div>
            `;
        }

        // Display explanation
        if (evaluation.explanation) {
            html += `<div class="explanation"><strong>Explanation:</strong><br>${evaluation.explanation.replace(/\n/g, '<br>')}</div>`;
        }

        // Display pros
        if (evaluation.pros) {
            html += `<div class="explanation"><strong>Pros:</strong><br>${evaluation.pros.replace(/\n/g, '<br>')}</div>`;
        }

        // Display cons
        if (evaluation.cons) {
            html += `<div class="explanation"><strong>Cons:</strong><br>${evaluation.cons.replace(/\n/g, '<br>')}</div>`;
        }

        resultsContent.innerHTML = html;
    }
});
