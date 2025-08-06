const MODES = {
	DISABLED: 0,
	ENABLED: 1, // Only one mode for enabling/disabling
}

const HEADERS = {
	REAL_IP: {
		header: 'X-Real-IP',
		value: '211.161.244.70',
	},
	CACHE_CONTROL: {
		header: 'Cache-Control',
		value: 'no-cache',
	},
}

// WebRequest listener for modifying headers
function onBeforeSendHeaders(details) {
	if (!details.requestHeaders) return {}

	// Add X-Real-IP header for music.163.com requests
	if (details.url.includes('music.163.com')) {
		details.requestHeaders.push({
			name: HEADERS.REAL_IP.header,
			value: HEADERS.REAL_IP.value,
		})
	}

	// Add Cache-Control header for music.126.net requests
	if (details.url.includes('.music.126.net')) {
		details.requestHeaders.push({
			name: HEADERS.CACHE_CONTROL.header,
			value: HEADERS.CACHE_CONTROL.value,
		})
	}

	return { requestHeaders: details.requestHeaders }
}

// Enable or disable web request listeners
function updateRules(mode) {
	try {
		// Remove existing listeners
		if (browser.webRequest.onBeforeSendHeaders.hasListener(onBeforeSendHeaders)) {
			browser.webRequest.onBeforeSendHeaders.removeListener(onBeforeSendHeaders)
		}

		// Add listeners if enabled
		if (mode === MODES.ENABLED) {
			browser.webRequest.onBeforeSendHeaders.addListener(
				onBeforeSendHeaders,
				{
					urls: ['*://music.163.com/*', '*://*.music.126.net/*'],
				},
				['blocking', 'requestHeaders']
			)
			console.log('WebRequest listeners added')
		}

		console.log('Rules updated for mode:', mode)
	} catch (error) {
		console.error('Failed to update rules:', error)
	}
}

// Update UI based on mode
async function updateUI(mode) {
	const icons = {
		[MODES.DISABLED]: {
			16: 'images/grey16.png',
			48: 'images/grey48.png',
			128: 'images/grey128.png',
		},
		[MODES.ENABLED]: {
			16: 'images/red16.png',
			48: 'images/red48.png',
			128: 'images/red128.png',
		},
	}

	const titles = {
		[MODES.DISABLED]: 'disabled',
		[MODES.ENABLED]: 'enabled',
	}

	await browser.browserAction.setIcon({ path: icons[mode] })
	const title = `${browser.i18n.getMessage('name')} [${browser.i18n.getMessage(titles[mode])}]`
	await browser.browserAction.setTitle({ title })
}

// Sync extension state
async function syncState(mode) {
	await Promise.all([browser.storage.local.set({ mode }), updateUI(mode), updateRules(mode)])
}

// Listen for icon click
browser.browserAction.onClicked.addListener(async () => {
	const { mode = MODES.ENABLED } = await browser.storage.local.get('mode')
	const newMode = mode === MODES.ENABLED ? MODES.DISABLED : MODES.ENABLED
	await syncState(newMode)
})

// Initialize extension
browser.runtime.onInstalled.addListener(async () => {
	const { mode } = await browser.storage.local.get('mode')
	const initialMode = mode ?? MODES.ENABLED
	await syncState(initialMode)
})

browser.runtime.onStartup.addListener(async () => {
	const { mode } = await browser.storage.local.get('mode')
	const initialMode = mode ?? MODES.ENABLED
	await syncState(initialMode)
})
