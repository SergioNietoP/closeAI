document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generateBtn');
    const addTopicBtn = document.getElementById('addTopicBtn');
    const topicsContainer = document.getElementById('topicsContainer');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const resultsContent = document.getElementById('resultsContent');

    addTopicBtn.addEventListener('click', function() {
        const topicInput = document.createElement('div');
        topicInput.className = 'topic-input';
        topicInput.innerHTML = `
            <input type="text" class="topic-title" placeholder="Topic Title">
            <textarea class="topic-description" rows="2" placeholder="Topic Description"></textarea>
        `;
        topicsContainer.appendChild(topicInput);
    });

    generateBtn.addEventListener('click', async function() {
        const topicInputs = document.querySelectorAll('.topic-input');
        const topics = [];

        topicInputs.forEach(input => {
            const title = input.querySelector('.topic-title').value.trim();
            const description = input.querySelector('.topic-description').value.trim();
            if (title && description) {
                topics.push({ title, description });
            }
        });

        if (topics.length === 0) {
            showError('Please add at least one topic with title and description.');
            return;
        }

        showLoading(loading);
        hideResults(results);
        generateBtn.disabled = true;

        try {
            const response = await fetch('/api/generate-questions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ topics })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Failed to generate questions');
            }

            displayQuestions(data.questions);
            showResults(results);
        } catch (error) {
            showError(error.message);
        } finally {
            hideLoading(loading);
            generateBtn.disabled = false;
        }
    });

    function displayQuestions(questionsData) {
        let html = '<div class="explanation">';
        
        try {
            // Try to parse as JSON
            const questions = typeof questionsData === 'string' ? JSON.parse(questionsData) : questionsData;
            
            // Display structured questions
            for (const [assessable, topics] of Object.entries(questions)) {
                html += `<h3 style="color: #667eea; margin-top: 1.5rem;">${assessable}</h3>`;
                
                if (typeof topics === 'object') {
                    for (const [topicName, topicQuestions] of Object.entries(topics)) {
                        html += `<h4 style="color: #764ba2; margin-top: 1rem;">${topicName}</h4>`;
                        html += '<ol>';
                        
                        if (typeof topicQuestions === 'object') {
                            for (const [key, question] of Object.entries(topicQuestions)) {
                                if (typeof question === 'string') {
                                    html += `<li style="margin: 0.5rem 0;">${question}</li>`;
                                }
                            }
                        }
                        
                        html += '</ol>';
                    }
                }
            }
        } catch (e) {
            // If parsing fails, display as formatted text
            html += questionsData.replace(/\n/g, '<br>');
        }
        
        html += '</div>';
        resultsContent.innerHTML = html;
    }
});
