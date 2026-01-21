# Lab 01: Workspace Navigation

## Databricks Platform Administration Training
### Duration: 30 Minutes | Difficulty: Beginner

---

## Lab Overview

In this introductory lab, you will explore the Databricks workspace interface and become familiar with the key components that administrators interact with daily. This hands-on exercise builds foundational navigation skills.

### Learning Objectives

By the end of this lab, you will be able to:
- Navigate the Databricks workspace UI confidently
- Identify key workspace components and their locations
- Create and organize basic workspace objects
- Access administrative interfaces (if permissions allow)

### Prerequisites

- Access to a Databricks workspace
- Valid user credentials
- Web browser (Chrome or Firefox recommended)

---

## Part 1: Accessing the Workspace (5 minutes)

### Task 1.1: Log In

1. Open your web browser and navigate to your workspace URL:
   - Format: `https://<workspace-name>.<region>.azuredatabricks.net` (Azure)
   - Format: `https://<workspace-name>.cloud.databricks.com` (AWS)
   - Format: `https://<workspace-name>.<region>.gcp.databricks.com` (GCP)

2. Enter your credentials and complete authentication

3. Upon successful login, you should see the Databricks landing page

**Checkpoint**: Record your workspace details:

| Item | Value |
|------|-------|
| Workspace URL | |
| Cloud Provider | AWS / Azure / GCP |
| Your Username | |

### Task 1.2: Identify the UI Layout

Familiarize yourself with the main UI areas:

1. **Left Sidebar** - Primary navigation menu
2. **Main Content Area** - Where content is displayed
3. **Top Bar** - Search, create, and user settings
4. **Bottom Status Bar** - Workspace info (if visible)

---

## Part 2: Exploring the Left Sidebar (10 minutes)

### Task 2.1: Navigate Each Section

Click through each item in the left sidebar and document what you find:

| Sidebar Item | Purpose | What You See |
|--------------|---------|--------------|
| **Home** | Personal landing page | |
| **Workspace** | Files and folders | |
| **Repos** | Git repositories | |
| **Catalog** | Data Explorer (Unity Catalog) | |
| **Workflows** | Jobs and pipelines | |
| **Compute** | Clusters and resources | |
| **SQL Warehouses** | SQL compute endpoints | |
| **SQL Editor** | Query interface | |
| **Dashboards** | Visualizations | |
| **Alerts** | Monitoring alerts | |

### Task 2.2: Explore the Workspace Browser

1. Click on **Workspace** in the sidebar

2. Navigate the folder structure:
   - **Users** - Personal folders for each user
   - **Shared** - Team collaboration space
   - Find your personal folder (`/Users/<your-email>`)

3. Create a new folder in your personal space:
   - Right-click → **Create** → **Folder**
   - Name it: `Admin-Training`

4. Create a notebook in your new folder:
   - Right-click on `Admin-Training` → **Create** → **Notebook**
   - Name: `Day01-Exploration`
   - Default Language: Python

**Checkpoint**: Verify you created:
- [ ] Folder: `Admin-Training`
- [ ] Notebook: `Day01-Exploration`

### Task 2.3: Explore Repos

1. Click on **Repos** in the sidebar

2. Observe the Git integration interface:
   - Repository listing
   - Branch selector
   - Sync controls

3. Document:

| Question | Answer |
|----------|--------|
| Are there any repos configured? | |
| What Git providers are supported? | |

---

## Part 3: Exploring Compute Resources (10 minutes)

### Task 3.1: View Clusters

1. Click on **Compute** in the sidebar

2. View the cluster list:
   - **All-purpose clusters** - For interactive work
   - **Job clusters** - Created by jobs (if any)

3. If there's an existing cluster, click on it to view details:

| Cluster Property | Value |
|------------------|-------|
| Cluster Name | |
| State (Running/Terminated) | |
| Databricks Runtime Version | |
| Node Type (Driver) | |
| Node Type (Worker) | |
| Number of Workers | |
| Auto-termination | |

4. Explore the cluster tabs:
   - **Configuration** - How the cluster is set up
   - **Notebooks** - Attached notebooks
   - **Libraries** - Installed packages
   - **Event Log** - Cluster events
   - **Driver Logs** - Spark driver output
   - **Spark UI** - Detailed Spark metrics (when running)

### Task 3.2: View SQL Warehouses

1. Click on **SQL Warehouses** in the sidebar

2. View available warehouses:

| Warehouse Property | Value |
|--------------------|-------|
| Warehouse Name | |
| State | |
| Size | |
| Type (Classic/Serverless) | |

3. If a warehouse exists, explore its configuration options

### Task 3.3: Understand Compute States

Document the different compute states:

| State | Icon/Color | Meaning |
|-------|------------|---------|
| Running | | |
| Terminated | | |
| Pending | | |
| Error | | |

---

## Part 4: Exploring Data (5 minutes)

### Task 4.1: Navigate the Catalog

1. Click on **Catalog** in the sidebar to open Data Explorer

2. Explore the catalog hierarchy:
   ```
   Catalog (e.g., main, hive_metastore)
   └── Schema (e.g., default)
       └── Table
   ```

3. Find and click on any existing table

4. Explore the table tabs:
   - **Columns** - Schema definition
   - **Sample Data** - Preview rows
   - **Details** - Metadata
   - **Permissions** - Access control
   - **History** - Version history (Delta tables)
   - **Lineage** - Data flow visualization

**Document your findings**:

| Question | Answer |
|----------|--------|
| How many catalogs exist? | |
| What schemas are available? | |
| Did you find any tables? | |

---

## Part 5: Admin Console Access (If Admin)

> **Note**: This section requires Workspace Admin privileges. Skip if you don't have admin access.

### Task 5.1: Access Admin Console

1. Click on your **username** (top-right corner)

2. Click on **Admin Console** (or Settings → Admin Console)

3. Explore the admin sections:

| Admin Section | What It Contains |
|---------------|------------------|
| Users | |
| Groups | |
| Service Principals | |
| Workspace Settings | |
| Compute | |

### Task 5.2: Review User List

1. In Admin Console, click **Users**

2. Document:

| Question | Answer |
|----------|--------|
| Total users in workspace | |
| How many admins? | |
| Your permission level | |

### Task 5.3: Review Group Membership

1. Click on **Groups**

2. Find the `admins` group

3. Document:

| Group | Members | Purpose |
|-------|---------|---------|
| admins | | |
| users | | |

---

## Lab Validation Checklist

Complete the following checklist:

### Navigation
- [ ] Successfully logged into workspace
- [ ] Navigated all sidebar items
- [ ] Found your personal folder in Workspace

### Objects Created
- [ ] Created `Admin-Training` folder
- [ ] Created `Day01-Exploration` notebook

### Compute Exploration
- [ ] Viewed cluster list and configurations
- [ ] Viewed SQL warehouse list
- [ ] Understand compute states

### Data Exploration
- [ ] Navigated Catalog/Data Explorer
- [ ] Explored table metadata (if tables exist)

### Admin Console (if applicable)
- [ ] Accessed Admin Console
- [ ] Reviewed user list
- [ ] Reviewed group memberships

---

## Reflection Questions

Answer these questions based on your exploration:

1. What is the difference between the **Workspace** and **Repos** sections?

   _Your answer:_

2. Why might an organization have multiple clusters configured?

   _Your answer:_

3. What information does the Catalog provide about a table?

   _Your answer:_

4. If you were a new data scientist joining this workspace, what would you need to do first?

   _Your answer:_

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Cannot log in | Check credentials, try incognito mode |
| Sidebar items missing | Some features require specific permissions |
| No clusters visible | May need admin to create or permission to view |
| Catalog is empty | Unity Catalog may not be configured |

---

## Lab Summary

In this lab, you explored:

1. **Workspace UI** - Navigation and layout
2. **Workspace objects** - Folders, notebooks, repos
3. **Compute resources** - Clusters and SQL warehouses
4. **Data Explorer** - Catalogs, schemas, tables
5. **Admin Console** - User and group management

These foundational skills will be used throughout the remaining 12 days of training.

---

## Next Steps

- Review Day 1 slides for concepts covered
- Complete the Day 1 quiz
- Read pre-materials for Day 2: Platform Administration Overview

---

*Lab Version: 2.0 | Databricks Platform Administration Training - Day 1*
