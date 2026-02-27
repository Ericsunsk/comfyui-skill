> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Toast API

The Toast API provides a way to display non-blocking notification messages to users. These are useful for providing feedback without interrupting workflow.

## Basic Usage

### Simple Toast

```javascript  theme={null}
// Display a simple info toast
app.extensionManager.toast.add({
  severity: "info",
  summary: "Information",
  detail: "Operation completed successfully",
  life: 3000
});
```

### Toast Types

```javascript  theme={null}
// Success toast
app.extensionManager.toast.add({
  severity: "success",
  summary: "Success",
  detail: "Data saved successfully",
  life: 3000
});

// Warning toast
app.extensionManager.toast.add({
  severity: "warn",
  summary: "Warning",
  detail: "This action may cause problems",
  life: 5000
});

// Error toast
app.extensionManager.toast.add({
  severity: "error",
  summary: "Error",
  detail: "Failed to process request",
  life: 5000
});
```

### Alert Helper

```javascript  theme={null}
// Shorthand for creating an alert toast
app.extensionManager.toast.addAlert("This is an important message");
```

## API Reference

### Toast Message

```javascript  theme={null}
app.extensionManager.toast.add({
  severity?: "success" | "info" | "warn" | "error" | "secondary" | "contrast", // Message severity level (default: "info")
  summary?: string,         // Short title for the toast
  detail?: any,             // Detailed message content
  closable?: boolean,       // Whether user can close the toast (default: true)
  life?: number,            // Duration in milliseconds before auto-closing
  group?: string,           // Group identifier for managing related toasts
  styleClass?: any,         // Style class of the message
  contentStyleClass?: any   // Style class of the content
});
```

### Alert Helper

```javascript  theme={null}
app.extensionManager.toast.addAlert(message: string);
```

### Additional Methods

```javascript  theme={null}
// Remove a specific toast
app.extensionManager.toast.remove(toastMessage);

// Remove all toasts
app.extensionManager.toast.removeAll();
```
