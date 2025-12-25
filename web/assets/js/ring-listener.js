import { RingApi } from 'ring-client-api';
import fetch from 'node-fetch';
import http from 'http';

const REFRESH_TOKEN = "eyJhbGciOiJSUzI1NiIsImprdSI6Ii9vYXV0aC9pbnRlcm5hbC9qd2tzIiwia2lkIjoiZDc0YjNhMWUiLCJ0eXAiOiJKV1QifQ.eyJpYXQiOjE3NjI4MDg2MjIsImlzcyI6IlJpbmdPYXV0aFNlcnZpY2UtcHJvZDp1cy1lYXN0LTE6NTk5YjAyZTciLCJvaWF0IjoxNzYyODA4NjIyLCJyZWZyZXNoX2NpZCI6InJpbmdfb2ZmaWNpYWxfYW5kcm9pZCIsInJlZnJlc2hfc2NvcGVzIjpbImNsaWVudCJdLCJyZWZyZXNoX3VzZXJfaWQiOjU4ODE2NCwicm5kIjoibEVvY3RmRWFVNyIsInNlc3Npb25faWQiOiI0MGNmNWFkZC0wMGFmLTQ2Y2ItOWU1OC00Mzc4NTE0ZTY3OTMiLCJ0eXBlIjoicmVmcmVzaC10b2tlbiJ9.e5PxIS2uZHRZ-bO2jMm_cerKC9wE-Dfpb_PVuRhwzt8JiwugE_CF9mHMgdAgXv7rr9hfAKHPsGnR3Mdn_EtroPS-9XKRIJmsbprwh-y5k1n3tKCmncEu4hbGaXD0cr88yxEbIA3kh8hj2D9hxtAL54oaIQHi01iiJ3owxnLcgPUzTEX6EyktvzRdW0hNRBdSnsWajIUFYRblsPp18PKIAX-ynhaXzY2X9QnPQWbwYyfw2J0Ym8QUwibrUxmTDnKSp0mTKG6BORty462C3EA-dH4AvshbMaAh8DGvxFP2OKD6PBcyxaxV547oU48bO-Q6oQTQmH7wNDBsbdX-5Ay8QA";

// тук ще пращаме събития до Python (FastAPI) – endpoint /api/ring-event
const PYTHON_ENDPOINT = 'http://127.0.0.1:8000/api/ring-event';

const ringApi = new RingApi({
  refreshToken: REFRESH_TOKEN,
  cameraDingsPollingSeconds: 5,
});

async function notifyPython(payload) {
  try {
    await fetch(PYTHON_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    console.log('➡️ Sent to Python:', payload);
  } catch (e) {
    console.error('❌ Error sending to Python:', e.message);
  }
}

// стартираме
(async () => {
  console.log('🔔 Starting Ring listener (Node)...');

  const locations = await ringApi.getLocations();
  const cameras = await ringApi.getCameras();

  console.log(`📷 Found ${cameras.length} Ring device(s).`);

  for (const camera of cameras) {
    camera.onNewDing.subscribe((ding) => {
      console.log('🚪 Ding event:', ding.motion || ding.ding, 'from device', camera.name);
      notifyPython({
        type: 'ring',
        device: camera.name,
        kind: ding.kind,         // motion / doorbell
        createdAt: ding.createdAt,
      });
    });
  }

  // малък HTTP health endpoint (по желание)
  const server = http.createServer((req, res) => {
    if (req.url === '/health') {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ ok: true }));
    } else {
      res.writeHead(404);
      res.end();
    }
  });
  server.listen(5055, () => console.log('✅ Ring listener health on http://127.0.0.1:5055/health'));
})();
