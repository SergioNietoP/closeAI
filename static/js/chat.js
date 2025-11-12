document.addEventListener('DOMContentLoaded', function() {
    const sendBtn = document.getElementById('sendBtn');
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');
    let conversationHistory = [];

    sendBtn.addEventListener('click', sendMessage);
    
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    async function sendMessage() {
        const message = chatInput.value.trim();

        if (!message) {
            return;
        }

        // Add user message to chat
        addMessage(message, 'user');
        chatInput.value = '';
        sendBtn.disabled = true;

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 
                    message,
                    history: conversationHistory
                })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Failed to get response');
            }

            // Add assistant response to chat
            addMessage(data.response, 'assistant');
            
            // Update conversation history
            conversationHistory.push({ role: 'user', content: message });
            conversationHistory.push({ role: 'assistant', content: data.response });
            
            // Keep only last 10 messages in history to avoid token limits
            if (conversationHistory.length > 20) {
                conversationHistory = conversationHistory.slice(-20);
            }
        } catch (error) {
            addMessage('Sorry, I encountered an error: ' + error.message, 'assistant');
        } finally {
            sendBtn.disabled = false;
            chatInput.focus();
        }
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function addMessage(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        const prefix = sender === 'user' ? '<strong>You:</strong> ' : '<strong>AI Assistant:</strong> ';
        const escapedContent = escapeHtml(content).replace(/\n/g, '<br>');
        messageContent.innerHTML = prefix + escapedContent;
        
        messageDiv.appendChild(messageContent);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
