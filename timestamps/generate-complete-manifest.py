"""
Complete IP Protection Manifest Generator
Hashes all research, publications, and supporting documents
Submits to OpenTimestamps for Bitcoin blockchain proof
Run this before any publication

Author: Kathleen Maree Grey
ORCID: 0009-0002-1423-7343
"""

import hashlib, json, datetime, os, requests, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# All directories containing IP to protect
DIRS = [
    'C:/Users/Admin/projects/world/04_Ventures/kol-shells-gold-paper-digital/_core',
    'C:/Users/Admin/projects/world/04_Ventures/kol-shells-gold-paper-digital/_core/_capsules/publishing',
    'C:/Users/Admin/projects/world/04_Ventures/kol-shells-gold-paper-digital/_core/_capsules/network-state-tracker',
    'C:/Users/Admin/projects/world/04_Ventures/kol-shells-gold-paper-digital/_core/_capsules/content-calendar',
    'C:/Users/Admin/projects/world/04_Ventures/kol-shells-gold-paper-digital/_core/_capsules/substack-setup',
    'C:/Users/Admin/projects/world/05_Experiments/network-state-research/papers',
    'C:/Users/Admin/projects/world/05_Experiments/network-state-research/research',
    'C:/Users/Admin/projects/world/05_Experiments/network-state-research/data',
    'C:/Users/Admin/projects/world/05_Experiments/network-state-research',
    'C:/Users/Admin/projects/world/05_Experiments/ip-stack-protocol',
    'C:/Users/Admin/projects/world/04_Ventures/dfat-malaysia/_core/_capsules/grant-pds-sea-investment',
    'C:/Users/Admin/projects/world/04_Ventures/dfat-malaysia/_core/_capsules/grant-korea-foundation',
]

# Collect and hash all files
results = {}
for d in DIRS:
    if not os.path.exists(d):
        continue
    for f in os.listdir(d):
        fp = os.path.join(d, f)
        if os.path.isfile(fp) and not f.startswith('.') and not f.endswith('.pyc'):
            try:
                with open(fp, 'rb') as fh:
                    h = hashlib.sha256(fh.read()).hexdigest()
                rel = fp.replace('C:/Users/Admin/projects/world/', '')
                results[rel] = {
                    'filename': f,
                    'sha256': h,
                    'size_bytes': os.path.getsize(fp),
                    'modified': datetime.datetime.fromtimestamp(
                        os.path.getmtime(fp), tz=datetime.timezone.utc
                    ).isoformat()
                }
            except Exception as e:
                print(f'  SKIP: {f} ({e})')

# Build manifest
manifest = {
    'author': 'Kathleen Maree Grey',
    'orcid': '0009-0002-1423-7343',
    'abn': '73 551 573 050',
    'generated': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'purpose': 'Complete IP protection manifest for all NSCF research, publications, and supporting documents',
    'total_files': len(results),
    'license': 'CC BY-NC-ND 4.0',
    'zenodo_doi': '10.5281/zenodo.19493961',
    'files': results
}

# Save manifest
out_dir = 'C:/Users/Admin/projects/world/05_Experiments/network-state-research/timestamps'
manifest_path = os.path.join(out_dir, 'copyright-manifest-complete.json')
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)
print(f'Manifest: {len(results)} files hashed')
print(f'Saved: {manifest_path}')

# Submit to OpenTimestamps
print('Submitting to OpenTimestamps...')
with open(manifest_path, 'rb') as f:
    file_hash = hashlib.sha256(f.read()).digest()

calendars = [
    'https://a.pool.opentimestamps.org/digest',
    'https://b.pool.opentimestamps.org/digest',
]

for cal in calendars:
    try:
        r = requests.post(cal, data=file_hash, headers={'Content-Type': 'application/x-www-form-urlencoded'}, timeout=15)
        if r.status_code == 200:
            ots_path = manifest_path + '.ots'
            with open(ots_path, 'wb') as out:
                out.write(r.content)
            print(f'OpenTimestamps proof saved: {ots_path}')
            print(f'Calendar: {cal}')
            break
        else:
            print(f'{cal}: status {r.status_code}')
    except Exception as e:
        print(f'{cal}: {e}')

print()
print('=== IP STACK STATUS ===')
print(f'Files hashed: {len(results)}')
print(f'Manifest: {manifest_path}')
print(f'Berne Convention: automatic (181 countries)')
print(f'OpenTimestamps: submitted')
print(f'Zenodo DOI: 10.5281/zenodo.19493961')
print(f'ORCID: 0009-0002-1423-7343')
print(f'License: CC BY-NC-ND 4.0')
print()
print('REMAINING (manual):')
print('  [ ] Push GitHub repo (git init, add, commit, push)')
print('  [ ] Upload NSCF PDF to SSRN')
print('  [ ] Update Zenodo record with v2.0')
print('  [ ] Create Google Scholar profile')
print('  [ ] Register on SafeCreative')
print('  [ ] Submit to Wayback Machine')
print()
print('Done.')
