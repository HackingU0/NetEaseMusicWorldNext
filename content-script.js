const MODES = {
	DISABLED: 0,
	ENABLED: 1,
}

// Inject page script into the webpage
function injectPageScript() {
	const script = document.createElement('script')
	script.src = browser.runtime.getURL('page-script.js')
	script.onload = () => script.remove()
	;(document.head || document.documentElement).appendChild(script)
}

// Initialize content script
async function initialize() {
	try {
		const { mode } = await browser.storage.local.get('mode')
		if (mode === MODES.ENABLED) {
			injectPageScript()
		}
	} catch (error) {
		console.error('Failed to initialize content script:', error)
	}
}

// Listen for mode changes
function setupModeChangeListener() {
	browser.storage.onChanged.addListener((changes, namespace) => {
		if (namespace === 'local' && changes.mode) {
			const newMode = changes.mode.newValue
			if (newMode === MODES.ENABLED) {
				injectPageScript()
			}
		}
	})
}

// Start initialization
initialize()
setupModeChangeListener()
