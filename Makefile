.PHONY: all baseprocedure worklist candidateprocedure finalprocedure

CURRENT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

APP_MODULE := dicom_deid
APP_DIR := $(CURRENT_DIR)/$(APP_MODULE)

DICOM_STANDARD_DIR := $(APP_DIR)/dicom_standard
PROCEDURE_DIR := $(CURRENT_DIR)/procedure
BASE_PROCEDURE := $(PROCEDURE_DIR)/base.json
MANUAL_PROCEDURE := $(PROCEDURE_DIR)/manual.json
CANDIDATE_PROCEDURE := $(PROCEDURE_DIR)/candidate.json

WORKLIST_OUTPUT := $(PROCEDURE_DIR)/MANUAL_WORKLIST.rts

DIST_DIR := dist

# Default full pipeline
all: finalprocedure worklist

# Target: Generate BASE
baseprocedure:
	uv run python -m $(APP_MODULE).build_base_procedure \
		--dicom-standard $(DICOM_STANDARD_DIR) \
		--output $(BASE_PROCEDURE)

# Target: BASE + MANUAL = CANDIDATE
candidateprocedure: baseprocedure
	uv run python -m $(APP_MODULE).build_candidate_procedure \
		--base $(BASE_PROCEDURE) \
		--manual $(MANUAL_PROCEDURE) \
		--output $(CANDIDATE_PROCEDURE)

# Target: Generate worklist that can be used to populate MANUAL
worklist: baseprocedure candidateprocedure
	uv run python -m $(APP_MODULE).update_worklist \
		--dicom-standard $(DICOM_STANDARD_DIR) \
		--candidate $(CANDIDATE_PROCEDURE) \
		--output $(WORKLIST_OUTPUT)

# Target: Final procedure that is fit for distribution
finalprocedure: baseprocedure candidateprocedure
	mkdir -p $(DIST_DIR)
	rm -rf $(DIST_DIR)/*
	uv run python -m  $(APP_MODULE).build_final_procedure \
		--candidate $(CANDIDATE_PROCEDURE) \
		--output $(DIST_DIR)

clean:
	rm -rf $(DIST_DIR)/*
	rm -f $(BASE_PROCEDURE) $(CANDIDATE_PROCEDURE) $(WORKLIST_OUTPUT)
