const mode = document.body.dataset.mode;

const tabs = [
  ['basic-element-drag', '1. Basic Element Drag'],
  ['coordinates', '2. Coordinates'],
  ['movement', '3. Movement'],
  ['html5', '4. DataTransfer'],
];

const modeNames = {
  'basic-element-drag': 'Basic element-to-element drag',
  coordinates: 'Precise-position drag',
  movement: 'Movement-sensitive drag',
  html5: 'HTML5 DataTransfer drag',
};

function icon(name) {
  const paths = {
    search: '<circle cx="11" cy="11" r="7"></circle><path d="m20 20-4-4"></path>',
    bell: '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9"></path><path d="M10 21h4"></path>',
    settings: '<circle cx="12" cy="12" r="3"></circle><path d="M19 12a7 7 0 0 0-.1-1l2-1.5-2-3.4-2.4 1a8 8 0 0 0-1.7-1L14.5 3h-5L9 6a8 8 0 0 0-1.7 1L5 6.1 3 9.5 5.1 11a7 7 0 0 0 0 2L3 14.5 5 18l2.3-1a8 8 0 0 0 1.7 1l.5 3h5l.5-3a8 8 0 0 0 1.7-1l2.3 1 2-3.5-2.1-1.5a7 7 0 0 0 .1-1Z"></path>',
    chevrons: '<path d="m7 8 4 4-4 4"></path><path d="m13 8 4 4-4 4"></path>',
    grid: '<rect x="4" y="4" width="6" height="6"></rect><rect x="14" y="4" width="6" height="6"></rect><rect x="4" y="14" width="6" height="6"></rect><rect x="14" y="14" width="6" height="6"></rect>',
    briefcase: '<rect x="3" y="7" width="18" height="13" rx="2"></rect><path d="M8 7V5h8v2M3 12h18M10 12v2h4v-2"></path>',
    chart: '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"></path>',
    calendar: '<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M7 3v4M17 3v4M3 10h18"></path><circle cx="12" cy="15" r="3"></circle>',
    help: '<circle cx="12" cy="12" r="9"></circle><path d="M9.8 9a2.4 2.4 0 0 1 4.6 1c0 2-2.4 2.1-2.4 4M12 18h.01"></path>',
    plus: '<circle cx="12" cy="12" r="9"></circle><path d="M12 8v8M8 12h8"></path>',
  };
  return `<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">${paths[name]}</svg>`;
}

let jobSequence = 101;

function jobCard({ source = false, company = 'SuperSQA', role = 'QA Automation Engineer', age = '17d' } = {}) {
  const testId = source ? ' data-testid="task-card"' : '';
  const sourceClass = source ? ' source-card' : '';
  const jobId = `JOB-${jobSequence++}`;

  return `
    <article class="job-card${sourceClass}" data-job-id="${jobId}"${testId}>
      <div class="card-top">
        <span class="company-mark">${company === 'SuperSQA' ? 'SS' : company.slice(0, 1)}</span>
        <span class="card-age">◷ ${age}</span>
      </div>
      <h3>${company}</h3>
      <p class="job-title">${role}</p>
      <div class="chips"><span class="chip">Remote</span><span class="chip">$110K – $145K</span></div>
      <div class="next-action">
        <div class="next-label">Next Action</div>
        <div class="next-value"><span>Follow up with manager</span><span>–</span></div>
      </div>
    </article>`;
}

document.querySelector('#app').innerHTML = `
  <header class="topbar">
    <div class="brand">SuperSQA Job Tracker</div>
    <div class="top-search">${icon('search')} Search applications...</div>
    <div class="profile">
      <span class="top-icon">${icon('bell')}<i class="notification-dot"></i></span>
      <span class="top-icon">${icon('settings')}</span>
      <div class="profile-copy"><div class="profile-name">SuperSQA Student</div><div class="profile-role">User</div></div>
      <div class="avatar">SS</div>
    </div>
  </header>
  <aside class="sidebar" aria-label="Primary navigation">
    <div class="collapse">${icon('chevrons')}</div>
    <div class="side-item active" title="Pipeline">${icon('grid')}</div>
    <div class="side-item" title="Jobs">${icon('briefcase')}</div>
    <div class="side-item" title="Analytics">${icon('chart')}</div>
    <div class="side-item" title="Interviews">${icon('calendar')}</div>
    <div class="side-item" title="Settings">${icon('settings')}</div>
    <div class="side-item side-help" title="Help">${icon('help')}</div>
  </aside>
  <main class="workspace">
    <div class="workspace-header">
      <div>
        <h1>Active Pipeline</h1>
        <p class="system-status">System status: optimal. Drag-and-drop lab active.</p>
      </div>
      <button class="new-button" type="button">${icon('plus')} New Application</button>
    </div>
    <nav class="method-row" aria-label="Drag-and-drop implementations">
      <span class="method-label">Implementation</span>
      ${tabs.map(([key, label]) => `<a class="method-tab" data-tab="${key}" href="../${key}/">${label}</a>`).join('')}
      <button class="reset-button" data-testid="reset-button" type="button">Reset Demo</button>
    </nav>
    <div class="toolbar">
      <label class="board-search">${icon('search')}<input type="text" placeholder="Search company, role, location, action"></label>
      <span class="metric">Demo: ${modeNames[mode]}</span>
      <span class="metric">Visible: 4</span>
    </div>
    <div class="status-line" data-testid="status">Ready: drag any application to another pipeline column</div>
    <section class="board" aria-label="Application pipeline">
      <section class="column potential">
        <header class="column-header"><h2 class="column-title">Potential</h2><div class="column-tools"><span class="count">1</span><span class="add">+</span></div></header>
        <div class="column-body" data-column="Potential" data-testid="todo-column">${jobCard({ source: true })}</div>
      </section>
      <section class="column applied">
        <header class="column-header"><h2 class="column-title">Applied</h2><div class="column-tools"><span class="count">1</span><span class="add">+</span></div></header>
        <div class="column-body" data-column="Applied" data-testid="done-column">
          ${jobCard({ company: 'TestCraft', role: 'SDET', age: '15d' })}
        </div>
      </section>
      <section class="column progress">
        <header class="column-header"><h2 class="column-title">In-Progress</h2><div class="column-tools"><span class="count">1</span><span class="add">+</span></div></header>
        <div class="column-body" data-column="In-Progress">${jobCard({ company: 'Quality Labs', role: 'Senior QA Engineer', age: 'Active' })}</div>
      </section>
      <section class="column final">
        <header class="column-header"><h2 class="column-title">Final Stage</h2><div class="column-tools"><span class="count">1</span><span class="add">+</span></div></header>
        <div class="column-body" data-column="Final Stage">${jobCard({ company: 'SuperSQA', role: 'Test Automation Lead', age: '2d' })}</div>
      </section>
    </section>
    <details class="event-details"><summary>Browser event log</summary><ol id="event-log"></ol></details>
  </main>`;

const cards = [...document.querySelectorAll('.job-card')];
const columnBodies = [...document.querySelectorAll('.column-body')];
const status = document.querySelector('[data-testid="status"]');
const eventLog = document.querySelector('#event-log');

document.querySelector(`[data-tab="${mode}"]`).classList.add('active');

function log(message) {
  const item = document.createElement('li');
  item.textContent = message;
  eventLog.prepend(item);
  while (eventLog.children.length > 7) eventLog.lastElementChild.remove();
}

function setStatus(message, type = '') {
  status.textContent = message;
  status.className = `status-line ${type}`.trim();
}

function pointIsInside(element, x, y) {
  const box = element.getBoundingClientRect();
  return x >= box.left && x <= box.right && y >= box.top && y <= box.bottom;
}

function columnAtPoint(x, y) {
  return columnBodies.find((column) => pointIsInside(column, x, y));
}

function pointIsInPreciseZone(column, x, y) {
  const box = column.getBoundingClientRect();
  return x >= box.left && x <= box.right && y >= box.top + 16 && y <= box.top + 94;
}

function updateCounts() {
  for (const column of columnBodies) {
    const count = column.querySelectorAll('.job-card').length;
    column.closest('.column').querySelector('.count').textContent = count;
  }
}

function finishDrop(card, targetColumn) {
  const sourceColumn = card.closest('.column-body');
  const company = card.querySelector('h3').textContent;

  if (sourceColumn === targetColumn) {
    setStatus(`${company} is already in ${targetColumn.dataset.column}`);
    return;
  }

  targetColumn.prepend(card);
  updateCounts();
  card.classList.remove('dragging');
  setStatus(`Success: ${company} moved to ${targetColumn.dataset.column}`, 'success');
  log(`drop accepted: ${targetColumn.dataset.column}`);
}

function installPointerDemo({ precise = false, minimumMoves = 0 } = {}) {
  let dragging = false;
  let moveCount = 0;
  let activeCard = null;
  let preview = null;
  let pointerOffsetX = 0;
  let pointerOffsetY = 0;

  for (const card of cards) {
    card.addEventListener('pointerdown', (event) => {
      if (event.button !== 0) return;
      event.preventDefault();
      dragging = true;
      moveCount = 0;
      activeCard = card;
      const box = card.getBoundingClientRect();
      pointerOffsetX = event.clientX - box.left;
      pointerOffsetY = event.clientY - box.top;

      preview = card.cloneNode(true);
      preview.removeAttribute('data-testid');
      preview.classList.add('drag-preview');
      preview.style.width = `${box.width}px`;
      preview.style.left = `${box.left}px`;
      preview.style.top = `${box.top}px`;
      document.body.append(preview);

      card.classList.add('dragging');
      document.body.classList.toggle('precise-drag', precise);
      setStatus(`Dragging ${card.querySelector('h3').textContent}…`);
      log(`pointerdown: ${card.dataset.jobId}`);
    });
  }

  document.addEventListener('pointermove', (event) => {
    if (!dragging) return;
    moveCount += 1;
    preview.style.left = `${event.clientX - pointerOffsetX}px`;
    preview.style.top = `${event.clientY - pointerOffsetY}px`;
    const targetColumn = columnAtPoint(event.clientX, event.clientY);
    for (const column of columnBodies) column.classList.remove('drop-hover');
    if (targetColumn && (!precise || pointIsInPreciseZone(targetColumn, event.clientX, event.clientY))) {
      targetColumn.classList.add('drop-hover');
    }
    log(`pointermove ${moveCount}`);
  });

  document.addEventListener('pointerup', (event) => {
    if (!dragging) return;
    const targetColumn = columnAtPoint(event.clientX, event.clientY);
    dragging = false;
    activeCard.classList.remove('dragging');
    for (const column of columnBodies) column.classList.remove('drop-hover');
    document.body.classList.remove('precise-drag');
    preview?.remove();
    preview = null;
    log('pointerup');

    if (!targetColumn) {
      setStatus('Drop rejected: release over a pipeline column', 'failed');
      return;
    }

    if (precise && !pointIsInPreciseZone(targetColumn, event.clientX, event.clientY)) {
      setStatus('Drop rejected: release on the insertion line', 'failed');
      return;
    }

    if (moveCount < minimumMoves) {
      setStatus(`Drop rejected: not enough movement events (${moveCount}/${minimumMoves})`, 'failed');
      return;
    }

    finishDrop(activeCard, targetColumn);
    activeCard = null;
  });
}

function installHtml5Demo() {
  let activeCard = null;

  for (const card of cards) {
    card.draggable = true;
    card.addEventListener('dragstart', (event) => {
      activeCard = card;
      event.dataTransfer.setData('application/x-job-id', card.dataset.jobId);
      event.dataTransfer.effectAllowed = 'move';
      card.classList.add('dragging');
      setStatus(`Dragging ${card.querySelector('h3').textContent}…`);
      log(`dragstart: ${card.dataset.jobId}`);
    });

    card.addEventListener('dragend', () => {
      card.classList.remove('dragging');
      for (const column of columnBodies) column.classList.remove('drop-hover');
    });
  }

  for (const column of columnBodies) {
    column.addEventListener('dragenter', (event) => {
      event.preventDefault();
      column.classList.add('drop-hover');
      log(`dragenter: ${column.dataset.column}`);
    });

    column.addEventListener('dragover', (event) => {
      event.preventDefault();
      event.dataTransfer.dropEffect = 'move';
      log('dragover');
    });

    column.addEventListener('dragleave', (event) => {
      if (!column.contains(event.relatedTarget)) column.classList.remove('drop-hover');
    });

    column.addEventListener('drop', (event) => {
      event.preventDefault();
      for (const item of columnBodies) item.classList.remove('drop-hover');
      const jobId = event.dataTransfer.getData('application/x-job-id');
      log(`drop payload: ${jobId || '(empty)'}`);

      if (activeCard?.dataset.jobId === jobId) finishDrop(activeCard, column);
      else setStatus('Drop rejected: DataTransfer payload missing', 'failed');
    });
  }
}

if (mode === 'basic-element-drag') installPointerDemo();
if (mode === 'coordinates') installPointerDemo({ precise: true });
if (mode === 'movement') installPointerDemo({ minimumMoves: 6 });
if (mode === 'html5') installHtml5Demo();

document.querySelector('[data-testid="reset-button"]').addEventListener('click', () => location.reload());
