class APIClient {
    constructor() {
        this.baseUrl = '/api/v1';
    }

    // Get CSRF Token from cookies
    getCsrfToken() {
        return document.cookie
            .split(';')
            .find(c => c.trim().startsWith('csrftoken='))
            ?.split('=')[1];
    }

    // Build headers
    getHeaders(requiresAuth = true, isMultipart = false) {
        const headers = {
            'X-CSRFToken': this.getCsrfToken(),
        };
        
        if (!isMultipart) {
            headers['Content-Type'] = 'application/json';
        }

        if (requiresAuth) {
            const token = sessionStorage.getItem('accessToken');
            if (token) {
                headers['Authorization'] = `Bearer ${token}`;
            }
        }
        return headers;
    }

    // Generic Fetch Request
    async request(url, options = {}) {
        try {
            const response = await fetch(`${this.baseUrl}${url}`, options);
            
            // Check for 401 Unauthorized (invalid/expired token)
            if (response.status === 401 && !url.includes('/auth/login')) {
                // Here we would handle token refresh, for now clear and redirect
                sessionStorage.removeItem('accessToken');
                window.location.href = '/login/';
                return;
            }

            const data = response.status !== 204 ? await response.json() : null;

            if (!response.ok) {
                throw data.errors || data;
            }

            return data;
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    // POST helper
    post(url, data, requiresAuth = true) {
        return this.request(url, {
            method: 'POST',
            headers: this.getHeaders(requiresAuth),
            body: JSON.stringify(data),
        });
    }

    // GET helper
    get(url, requiresAuth = true) {
        return this.request(url, {
            method: 'GET',
            headers: this.getHeaders(requiresAuth),
        });
    }
}

const api = new APIClient();
