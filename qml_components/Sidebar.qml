import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "custom_widgets"

Item{
    ColumnLayout{
        anchors.fill: parent
        anchors.leftMargin: 5
        spacing: 20

        // Search by title
        IconTextField{
            id: search_by_title
            placeholder_text: "Search by title"
            icon: Resources.get("search.svg")
            onChanged: MovieListProxy.set_filter(field_text)
        }

        // Sorting
        CustomRectangle{
            Layout.fillWidth: true
            implicitHeight: 100

            ColumnLayout{
                anchors.fill: parent
                anchors.margins: 10

                SubtitleText{
                    text: "Sort result by:"
                }

                ComboBox{
                    model: MovieListProxy.sorting_options
                    Layout.fillWidth: true

                    // onActivated: print("Sort by:", currentText, currentIndex)
                    onActivated: MovieListProxy.current_sorting = currentText
                }
            }
        }

        // Genre filter
        CustomRectangle{
            Layout.fillWidth: true
            implicitHeight: childrenRect.height + 20

            ColumnLayout{
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.margins: 10

                SubtitleText{
                    text: "Genres"
                }

                Repeater{
                    model: MovieList.genre_list
                    TextButton{
                        text: modelData; 
                        default_color: "gray"; 
                        highlight_color: "black"
                        font_size: 14
                        active_color: "black"
                        state: MovieListProxy.current_genre === modelData? "active" : ""
                        onClicked: MovieListProxy.current_genre = modelData
                    }
                }
            }
        }

        // spacer
        Item{
            Layout.fillHeight: true
        }
    }
}